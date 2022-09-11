from abc import ABC, abstractmethod
from scraper.domains import (
    AmazonHandler,
    AvCablesHandler,
    AvXpertenHandler,
    ComputerSalgHandler,
    CoolshopHandler,
    EbayHandler,
    ElgigantenHandler,
    ExpertHandler,
    KomplettHandler,
    MMVisionHandler,
    NeweggHandler,
    PowerHandler,
    ProshopHandler,
    SharkGamingHandler,
    HifiKlubbenHandler,
)
from scraper.format import Info


komplett_handler = KomplettHandler("https://www.komplett.dk/product/1168438")
komplett_handler._request_product_data()
komplett_handler._get_common_data()

proshop_handler = ProshopHandler("https://www.proshop.dk/Hovedtelefonerheadset/Sony-WH-1000XM4/2883832")
proshop_handler._request_product_data()
proshop_handler._get_common_data()

computersalg_handler = ComputerSalgHandler(
    "https://www.computersalg.dk/i/6647865/sony-wh-1000xm4-hovedtelefoner-med-mik-fuld-st%c3%b8rrelse-bluetooth-tr%c3%a5dl%c3%b8s-kabling-nfc-aktiv-st%c3%b8jfjerning-3-5-mm-jackstik-sort"
)
computersalg_handler._request_product_data()
computersalg_handler._get_common_data()

elgiganten_handler = ElgigantenHandler(
    "https://www.elgiganten.dk/product/tv-lyd-smart-home/horetelefoner-tilbehor/horetelefoner/sony-tradlose-around-ear-horetelefoner-wh-1000xm4-sort/200693"
)
elgiganten_handler._request_product_data()
elgiganten_handler._get_common_data()

avxperten_handler = AvXpertenHandler(
    "https://www.avxperten.dk/noise-cancelling-head-set/sony-wh-1000xm4-bluetooth-hovedtelefoner-anc-sort.asp"
)
avxperten_handler._request_product_data()
avxperten_handler._get_common_data()

avcables_handler = AvCablesHandler(
    "https://www.av-cables.dk/bluetooth-hoeretelefoner/sony-wh-1000xm4-over-ear-bluetooth-headset-sort.html"
)
avcables_handler._request_product_data()
avcables_handler._get_common_data()

amazon_handler = AmazonHandler(
    "https://www.amazon.com/Sony-WH-1000XM4-Wireless-Canceling-Headphones/dp/B08HDKHSSN/ref=sr_1_3?crid=2QKY9WQGCV809&keywords=sony+xm4&qid=1660593858&sprefix=sony+xm%2Caps%2C171&sr=8-3"
)
amazon_handler._request_product_data()
amazon_handler._get_common_data()

# for url that start with 'ebay.com/itm/'
ebay_handler_with_item = EbayHandler("https://www.ebay.com/itm/265771092654")
ebay_handler_with_item._request_product_data()
ebay_handler_with_item._get_common_data()

# for url that start with 'ebay.com/p/'
ebay_handler_with_p = EbayHandler("https://www.ebay.com/p/1248083754?iid=181677611772&rt=nc")
ebay_handler_with_p._request_product_data()
ebay_handler_with_p._get_common_data()

expert_handler = ExpertHandler(
    "https://www.expert.dk/hoejtalere-og-lyd/hovedtelefoner/traadloese-hovedtelefoner/sony-wh-1000xm4-traadloese-stoejdaempende-hovedtelefoner-sort/p-1106907/"
)
expert_handler._request_product_data()
expert_handler._get_common_data()

power_handler = PowerHandler(
    "https://www.power.dk/tv-og-lyd/hovedtelefoner/traadloese-hovedtelefoner/sony-wh-1000xm4-traadloese-stoejdaempende-hovedtelefoner-blaa/p-1185731/"
)
power_handler._request_product_data()
power_handler._get_common_data()

mmvision_handler = MMVisionHandler("https://www.mm-vision.dk/asus-zenbook-duo-14-ux482eg-pure9x-baerbar")
mmvision_handler._request_product_data()
mmvision_handler._get_common_data()

coolshop_handler = CoolshopHandler("https://www.coolshop.dk/produkt/pokemon-brilliant-diamond/238G6U/")
coolshop_handler._request_product_data()
coolshop_handler._get_common_data()

sharkgaming_handler = SharkGamingHandler("https://sharkgaming.dk/asus-gladius-ii-origin-gaming-mouse")
sharkgaming_handler._request_product_data()
sharkgaming_handler._get_common_data()

newegg_handler = NeweggHandler(
    "https://www.newegg.com/sony-wh1000xm4b-bluetooth-headset-black/p/0G6-001C-00614?Description=sony%20xm4&cm_re=sony_xm4-_-0G6-001C-00614-_-Product&quicklink=true"
)
newegg_handler._request_product_data()
newegg_handler._get_common_data()

hifiklubben_handler = HifiKlubbenHandler(
    "https://www.hifiklubben.dk/sennheiser-momentum-4-wireless-hoeretelefoner/senmomentum4bk/"
)
hifiklubben_handler._request_product_data()
hifiklubben_handler._get_common_data()


class BaseTestWebsiteHandler(ABC):
    @abstractmethod
    def test_get_product_info(self):
        pass

    @abstractmethod
    def test_get_name(self):
        pass

    @abstractmethod
    def test_get_price(self):
        pass

    @abstractmethod
    def test_get_currency(self):
        pass

    @abstractmethod
    def test_get_id(self):
        pass


class TestKomplettHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=komplett_handler.request_data)
        actual = komplett_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = komplett_handler._get_product_name().lower()
        expected = "ASUS GeForce RTX 3090 ROG Strix OC".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = komplett_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = komplett_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = komplett_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "1168438"


class TestProshopHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=proshop_handler.request_data)
        actual = proshop_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = proshop_handler._get_product_name().lower()
        expected = "Sony WH-1000XM4".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = proshop_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = proshop_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = proshop_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "2883832"


class TestComputersalgHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=computersalg_handler.request_data)
        actual = computersalg_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = computersalg_handler._get_product_name().lower()
        expected = "Sony WH-1000XM4 - Hovedtelefoner med mik. - fuld størrelse - Bluetooth - trådløs, kabling - NFC - aktiv støjfjerning - 3,5 mm jackstik - sort".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = computersalg_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = computersalg_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = computersalg_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "6647865"


class TestElgigantenHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=elgiganten_handler.request_data)
        actual = elgiganten_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = elgiganten_handler._get_product_name().lower()
        expected = "Sony trådløse around-ear høretelefoner WH-1000XM4 (sort)".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = elgiganten_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = elgiganten_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = elgiganten_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "200693"


class TestAvXpertenHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=avxperten_handler.request_data)
        actual = avxperten_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = avxperten_handler._get_product_name().lower()
        expected = "Sony WH-1000XM4 Bluetooth hovedtelefoner (m/ANC) Sort".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = avxperten_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = avxperten_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = avxperten_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "33590"


class TestAvCablesHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=avcables_handler.request_data)
        actual = avcables_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = avcables_handler._get_product_name().lower()
        expected = "Sony WH-1000XM4 Over-Ear Bluetooth Headset - Sort".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = avcables_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = avcables_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = avcables_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "833015"


class TestAmazonHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=amazon_handler.request_data)
        actual = amazon_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = amazon_handler._get_product_name().lower()
        expected = "Sony WH-1000XM4 Wireless Noise Canceling Overhead Headphones - Black (Renewed)".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = amazon_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = amazon_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "USD"

    def test_get_id(self):
        id = amazon_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "B08HDKHSSN"


# OBS: There is two Ebay versions - This is for url that start with 'ebay.com/itm/'
class TestEbayHandler_with_itm(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=ebay_handler_with_item.request_data)
        actual = ebay_handler_with_item.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = ebay_handler_with_item._get_product_name().lower()
        expected = "BRAND NEW Sony PS5 Playstation 5 Blu-Ray Disc Edition Console  -Fast Delivery".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = ebay_handler_with_item._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = ebay_handler_with_item._get_product_currency()
        assert isinstance(currency, str)
        assert len(currency) == 3
        assert currency == "USD"

    def test_get_id(self):
        id = ebay_handler_with_item._get_product_id()
        assert isinstance(id, str)
        assert id == "265771092654"


# OBS: There is two Ebay versions - This is for url that start with 'ebay.com/p/'
class TestEbayHandler_with_p(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=ebay_handler_with_p.request_data)
        actual = ebay_handler_with_p.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = ebay_handler_with_p._get_product_name().lower()
        expected = "Etude House Collagen Eye Patch Korea Cosmetics 10 Sheets".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = ebay_handler_with_p._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = ebay_handler_with_p._get_product_currency()
        assert isinstance(currency, str)
        assert len(currency) == 3
        # assert currency == "DKK"

    def test_get_id(self):
        id = ebay_handler_with_p._get_product_id()
        assert isinstance(id, str)
        assert id == "181677611772"


class TestPowerHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=power_handler.request_data)
        actual = power_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = power_handler._get_product_name().lower()
        expected = "SONY WH-1000XM4 TRÅDLØSE STØJDÆMPENDE HOVEDTELEFONER BLÅ".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = power_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = power_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = power_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "1185731"


class TestExpertHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=expert_handler.request_data)
        actual = expert_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = expert_handler._get_product_name().lower()
        expected = "SONY WH-1000XM4 TRÅDLØSE STØJDÆMPENDE HOVEDTELEFONER SORT".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = expert_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = expert_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = expert_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "1106907"


class TestMMVisionHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=mmvision_handler.request_data)
        actual = mmvision_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = mmvision_handler._get_product_name().lower()
        expected = "Asus ZenBook Duo 14 UX482".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = mmvision_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = mmvision_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = mmvision_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "6987132"


class TestCoolshopHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=coolshop_handler.request_data)
        actual = coolshop_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = coolshop_handler._get_product_name().lower()
        expected = "Pokemon Brilliant Diamond - Nintendo Switch".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = coolshop_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = coolshop_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = coolshop_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "1177871"


class TestSharkGamingHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=sharkgaming_handler.request_data)
        actual = sharkgaming_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = sharkgaming_handler._get_product_name().lower()
        expected = "ASUS Gladius II Origin gaming mouse".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = sharkgaming_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = sharkgaming_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = sharkgaming_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "90MP00U1-B0UA00"


class TestNeweggHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=newegg_handler.request_data)
        actual = newegg_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = newegg_handler._get_product_name().lower()
        expected = "Sony WH-1000XM4 Wireless Noise-Cancelling Over-Ear Headphones (Black)".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = newegg_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = newegg_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "USD"

    def test_get_id(self):
        id = newegg_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "0G6-001C-00614"


class TestHifiKlubbenHandler(BaseTestWebsiteHandler):
    def test_get_product_info(self, mocker):
        mocker.patch("scraper.domains.BaseWebsiteHandler._request_product_data", return_value=hifiklubben_handler.request_data)
        actual = hifiklubben_handler.get_product_info()
        assert isinstance(actual, Info)
        assert actual.valid

    def test_get_name(self):
        actual = hifiklubben_handler._get_product_name().lower()
        expected = "SENNHEISER MOMENTUM 4 WIRELESS".lower()
        assert isinstance(actual, str)
        assert actual == expected

    def test_get_price(self):
        price = hifiklubben_handler._get_product_price()
        assert isinstance(price, float)

    def test_get_currency(self):
        currency = hifiklubben_handler._get_product_currency()
        assert isinstance(currency, str)
        assert currency == "DKK"

    def test_get_id(self):
        id = hifiklubben_handler._get_product_id()
        assert isinstance(id, str)
        assert id == "senmomentum4bk"
