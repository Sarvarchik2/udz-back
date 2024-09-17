# Generated by Django 5.1 on 2024-09-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_tenderlar_pdflink1_tenderlar_pdflink10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boshishjoylari',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='boshishjoylari',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='boshishjoylari',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='boshishjoylari',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='davlatramzlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='davlatramzlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='davlatramzlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='davlatramzlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='davlattashkilotlari',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='davlattashkilotlari',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='davlattashkilotlari',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='davlattashkilotlari',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='elektronhukumatdoirasidaamalgaoshirilayotganloyihalar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='elektronhukumatdoirasidaamalgaoshirilayotganloyihalar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='elektronhukumatdoirasidaamalgaoshirilayotganloyihalar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='elektronhukumatdoirasidaamalgaoshirilayotganloyihalar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='gendertenglikasosiyinsonhuquqlaridanbiri',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='gendertenglikasosiyinsonhuquqlaridanbiri',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='gendertenglikasosiyinsonhuquqlaridanbiri',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='gendertenglikasosiyinsonhuquqlaridanbiri',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='gendertenglikkaoidmeyoriyhujjatlarniishlabchiqish',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='gendertenglikkaoidmeyoriyhujjatlarniishlabchiqish',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='gendertenglikkaoidmeyoriyhujjatlarniishlabchiqish',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='gendertenglikkaoidmeyoriyhujjatlarniishlabchiqish',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='harakatlarstrategiyasi',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='harakatlarstrategiyasi',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='harakatlarstrategiyasi',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='harakatlarstrategiyasi',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='interaktivxizmat',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='interaktivxizmat',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='interaktivxizmat',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='interaktivxizmat',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='ishonchtelefonireglamenti',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='ishonchtelefonireglamenti',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='ishonchtelefonireglamenti',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='ishonchtelefonireglamenti',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='kopkelgansavollargajavoblar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='kopkelgansavollargajavoblar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='kopkelgansavollargajavoblar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='kopkelgansavollargajavoblar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='korsatkichlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='korsatkichlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='korsatkichlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='korsatkichlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='logistikasamaradorligiindeksiboyichaochiqmalumotlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='logistikasamaradorligiindeksiboyichaochiqmalumotlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='logistikasamaradorligiindeksiboyichaochiqmalumotlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='logistikasamaradorligiindeksiboyichaochiqmalumotlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='meyoriyhujjatlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='meyoriyhujjatlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='meyoriyhujjatlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='meyoriyhujjatlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='meyorvazirlikdagendersiyosatiiyhujjatlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='meyorvazirlikdagendersiyosatiiyhujjatlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='meyorvazirlikdagendersiyosatiiyhujjatlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='meyorvazirlikdagendersiyosatiiyhujjatlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='murojaatlarnikoribchiqishtartibi',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='murojaatlarnikoribchiqishtartibi',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='murojaatlarnikoribchiqishtartibi',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='murojaatlarnikoribchiqishtartibi',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='murojaatlarstatistikasi',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='murojaatlarstatistikasi',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='murojaatlarstatistikasi',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='murojaatlarstatistikasi',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='news',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='news',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='news',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='news',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='ochiqmalumotlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='ochiqmalumotlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='ochiqmalumotlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='ochiqmalumotlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='qonunchilikbazasi',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='qonunchilikbazasi',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='qonunchilikbazasi',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='qonunchilikbazasi',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='umumiymalumotlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='umumiymalumotlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='umumiymalumotlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='umumiymalumotlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='vazirlikdagendersiyosati',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='vazirlikdagendersiyosati',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='vazirlikdagendersiyosati',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='vazirlikdagendersiyosati',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='yoshlarmarkaziyangiliklari',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='yoshlarmarkaziyangiliklari',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='yoshlarmarkaziyangiliklari',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='yoshlarmarkaziyangiliklari',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosati',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosati',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosati',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosati',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosatigaoidmeyoriyhuquqiyhujjatlar',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosatigaoidmeyoriyhuquqiyhujjatlar',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosatigaoidmeyoriyhuquqiyhujjatlar',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='yoshlarsiyosatigaoidmeyoriyhuquqiyhujjatlar',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
        migrations.AddField(
            model_name='yurtimizdagendertengliknitaminlashstrategiyasi',
            name='pdflink1',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 1'),
        ),
        migrations.AddField(
            model_name='yurtimizdagendertengliknitaminlashstrategiyasi',
            name='pdflink2',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 2'),
        ),
        migrations.AddField(
            model_name='yurtimizdagendertengliknitaminlashstrategiyasi',
            name='pdflink3',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 3'),
        ),
        migrations.AddField(
            model_name='yurtimizdagendertengliknitaminlashstrategiyasi',
            name='pdflink4',
            field=models.URLField(blank=True, null=True, verbose_name='PDF ссылка 4'),
        ),
    ]
