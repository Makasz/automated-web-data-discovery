from scrapy import log
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.response import get_meta_refresh


class CustomRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):
        url = response.url
        if response.status in [301, 307]:
            log.msg("trying to redirect us: %s" %url, level=log.INFO)
            reason = 'redirect %d' %response.status
            return self._retry(request, reason, spider) or response
        interval, redirect_url = get_meta_refresh(response)
        if response.status in [502, 503]:
            log.msg("Service Unavailable: %s" %url, level=log.INFO)
            reason = 'Possible block with 5xx error'
            return self._retry(request, reason, spider) or response
        # handle meta redirect
        if redirect_url:
            log.msg("trying to redirect us: %s" %url, level=log.INFO)
            reason = 'meta'
            return self._retry(request, reason, spider) or response
        hxs = HtmlXPathSelector(response)
        # test for captcha page
        captcha = hxs.select(".//input[contains(@id, 'captchacharacters')]").extract()
        if captcha or "Dostęp zablokowany" in response.text:
            log.msg("captcha page %s" %url, level=log.INFO)
            reason = 'captcha'
            return self._retry(request, reason, spider) or response
        if response.status in [502, 503, 504]:
            log.msg("Captcha with status: \n%s" %response.text, level=log.INFO)
            reason = 'captcha'
            return self._retry(request, reason, spider) or response
        return response