from hamcrest.core.base_matcher import BaseMatcher


class PriceMatcher(BaseMatcher):

    def __init__(self, maxInclusive=3_000):
        self.maxInclusive = maxInclusive

    def _matches(self, price):
        return 0 < price <= self.maxInclusive

    def describe_to(self, description):
        description.append_text("0..." + str(self.maxInclusive))


def valid_price():
    return PriceMatcher(2_500)
