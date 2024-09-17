from rest_framework import serializers
from .models import (
    Person,
    News,
    Tenderlar,
    DavlatRamzlar,
    Product,
    ProductInfo,
    Document,
    Deal,
    Image,
    Logo,
    Employee,
    Vazirlik,
    InteraktivXizmat,
    ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalar,
    DavlatTashkilotlari,
    MurojaatlarniKoribchiqishTartibi,
    MurojaatlarStatistikasi,
    IshonchTelefoniReglamenti,
    LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlar,
    YoshlarSiyosati,
    YoshlarMarkaziYangiliklari,
    YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlar,
    UmumiyMalumotlar,
    GenderTenglikAsosiyInsonHuquqlaridanBiri,
    YurtimizdaGenderTenglikniTaminlashStrategiyasi,
    MeyoriyHujjatlar,
    MeyorVazirlikdaGenderSiyosatiiyHujjatlar,
    VazirlikdaGenderSiyosati,
    Korsatkichlar,
    GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqish,
)
from .models import (
    SaytHaritasi,
    HarakatlarStrategiyasi,
    QonunchilikBazasi,
    BoshIshJoylari,
    OchiqMalumotlar,
    KopKelganSavollargaJavoblar,
)
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
from .models import Korupsiya

class KorupsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korupsiya
        fields = ['id', 'title', 'description', 'image', 'pdf_file', 'pdf_online_link', 'download_link', 'created_at']

from .models import VideoLink

class VideoLinkserializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLink
        fields = "__all__"

class SaytHaritasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaytHaritasi
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class HarakatlarStrategiyasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarakatlarStrategiyasi
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class QonunchilikBazasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QonunchilikBazasi
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class BoshIshJoylariSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoshIshJoylari
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class OchiqMalumotlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OchiqMalumotlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class KopKelganSavollargaJavoblarSerializer(serializers.ModelSerializer):
    class Meta:
        model = KopKelganSavollargaJavoblar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class DavlatRamzlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = DavlatRamzlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class KorsatkichlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korsatkichlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class TenderlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenderlar
        fields = [
            "id",
            "text_en",
            "text_ru",
            "text_uz",
            "title_uz",
            "title_ru",
            "title_en",
            "pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",
            "pdflink5",
            "pdflink6",
            "pdflink7",
            "pdflink8",
            "pdflink9",
            "pdflink10",
            "pdflink11",
            "pdflink12",
            "start_date",
            "end_date",
            "views",
            "status",
        ]

# 222222
class GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqishSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqish
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class VazirlikdaGenderSiyosatiSerializer(serializers.ModelSerializer):
    class Meta:
        model = VazirlikdaGenderSiyosati
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class MeyoriyHujjatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeyoriyHujjatlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalarSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class MeyorVazirlikdaGenderSiyosatiiyHujjatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeyorVazirlikdaGenderSiyosatiiyHujjatlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class DavlatTashkilotlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = DavlatTashkilotlari
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class MurojaatlarniKoribchiqishTartibiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MurojaatlarniKoribchiqishTartibi
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class MurojaatlarStatistikasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MurojaatlarStatistikasi
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class IshonchTelefoniReglamentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = IshonchTelefoniReglamenti
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlarSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class YoshlarSiyosatiSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoshlarSiyosati
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class YoshlarMarkaziYangiliklariSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoshlarMarkaziYangiliklari
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlarSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class UmumiyMalumotlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmumiyMalumotlar
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class GenderTenglikAsosiyInsonHuquqlaridanBiriSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderTenglikAsosiyInsonHuquqlaridanBiri
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class YurtimizdaGenderTenglikniTaminlashStrategiyasiSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = YurtimizdaGenderTenglikniTaminlashStrategiyasi
        fields = ["id", "text_en", "text_ru", "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]
# 22222222

class InteraktivXizmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteraktivXizmat
        fields = ["id", "title_en", "title_ru", "title_uz", "url", "views","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",]


class VazirlikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vazirlik
        fields = [
            "id",
            "title_en",
            "title_ru",
            "title_uz",
            "text_en",
            "text_ru",
            "text_uz","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "full_name_en",
            "full_name_ru",
            "full_name_uz",
            "phone_number",
            "address_en",
            "address_ru",
            "address_uz",
            "position_en",
            "position_ru",
            "position_uz",
            "email",
            "comment_en",
            "comment_ru",
            "comment_uz",
            "photo",
        ]


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ["id", "link", "image", "text_en", "text_ru", "text_uz"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title_en", "title_ru", "title_uz", "image"]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["id", "title_en", "title_ru", "title_uz", "pdf_file"]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "id",
            "title_en",
            "title_ru",
            "title_uz",
            "image",
            "text_en",
            "text_ru",
            "text_uz",
            "link",
            "pub_date",
            "views","pdflink1",
            "pdflink2",
            "pdflink3",
            "pdflink4",
        ]


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = [
            "id",
            "title_en",
            "title_ru",
            "title_uz",
            "description_en",
            "description_ru",
            "description_uz",
            "site",
            "img",
            "gmail",
            "price",
            "status",
            "publish_date",
            "expiration_date",
            "views",
        ]





# class ProductInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductInfo
#         fields = ['id', 'title_en', 'title_ru', 'title_uz', 'text_en', 'text_ru', 'text_uz', 'product_number', 'brand', 'quantity', 'price_per_unit', 'group_deal', 'trade_type', 'warranty_type', 'manufacturer', 'manufacturer_country', 'start_date', 'end_date', ]

# class ProductSerializer(serializers.ModelSerializer):
#     info = ProductInfoSerializer(many=True, read_only=True)

#     class Meta:
#         model = Product
#         fields = ['id', 'name_en', 'name_ru', 'name_uz', 'description_en', 'description_ru', 'description_uz', 'image', 'info']


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = [
            "id",
            "title_en",
            "title_ru",
            "title_uz",
            "text_en",
            "text_ru",
            "text_uz",
        ]


class ProductSerializer(serializers.ModelSerializer):
    info = ProductInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name_en",
            "name_ru",
            "name_uz",
            "description_en",
            "description_ru",
            "description_uz",
            "image",
            "info",
            "product_number",
            "brand",
            "quantity",
            "price_per_unit",
            "group_deal",
            "trade_type",
            "warranty_type",
            "manufacturer",
            "manufacturer_country",
            "start_date",
            "end_date",
        ]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name"]
