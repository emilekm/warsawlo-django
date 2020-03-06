# Generated by Django 3.0 on 2019-12-16 20:43

from django.db import migrations

import csv
from search.models import School, PublicInstitutionData, Address, ContactData


def load_data(apps, schema_editor):
    with open('csvs/publiczne.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_number = 0
        for row in csv_reader:
            if row_number == 0:
                row_number += 1
            elif row[46] != 'jednostka inna niż przedszkole lub szkoła':
                school = School()

                public_data = PublicInstitutionData()
                public_data.institution_short_name = row[0]
                public_data.short_name = row[1]
                public_data.institution_regon = row[2]
                public_data.regon = row[3]
                public_data.institution_RSPO = row[4]
                public_data.RSPO = row[5]
                public_data.institution_name = row[6]
                school.school_name = row[7]
                public_data.institution_type = row[8]
                school.school_type = row[9]
                school.student_type = row[10]
                school.is_public = True
                school.is_special_needs_school = True if row[11] == "tak" else False
                public_data.data = {'supervisor': row[12]}

                address = Address()
                address.city = row[13]
                address.district = row[14]
                public_data.data['information_system'] = row[15]
                address.street = row[16]
                address.building_nr = row[17]
                address.postcode = row[18]

                contact = ContactData()
                contact.phone = row[21]
                contact.website = row[23]
                public_data.data['BIP'] = row[24]
                contact.email = row[25]

                public_data.data['has_dormitory'] = True if row[27] == 'tak' else False

                divisions = []
                if row[35] == 'tak':
                    divisions.append('dwujęzyczne')
                if row[36] == 'tak':
                    divisions.append('integracyjne')
                if row[37] == 'tak':
                    divisions.append('sportowe')
                if row[38] == 'tak':
                    divisions.append('mistrzostwa sportowego')
                if row[39] == 'tak':
                    divisions.append('międzynarodowe')
                if row[40] == 'tak':
                    divisions.append('specjalne')
                if row[41] == 'tak':
                    divisions.append('specjalne przysposabiające do pracy')
                if row[42] == 'tak':
                    divisions.append('terapeutyczne')
                if row[43] == 'tak':
                    divisions.append('eksperymentalne')
                school.specialised_divisions = divisions

                school.data = {'is_in_school_complex': True if row[45] == 'tak' else False}
                if row[46] == 'szkoła podstawowa (w tym muzyczna)':
                    school.school_type_generalised = 'szkoła podstawowa'
                else:
                    school.school_type_generalised = row[46]

                public_data.data['RSPO_url'] = row[60]
                public_data.data['psychological_clinic'] = row[62]
                public_data.data['main_disability'] = row[63]
                public_data.data['is_by_hospital'] = True if row[64] == 'tak' else False

                address.longitude = row[66].replace(',', '.')
                address.latitude = row[65].replace(',', '.')

                public_data.data['ankietyBE_id'] = row[69]

                school.address = address
                school.contact = contact
                school.public_institution_data = public_data

                public_data.save()
                address.save()
                contact.save()
                school.save()


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_contact_school_address_institutiondata_highschoolclass'),
    ]
    operations = [
        migrations.RunPython(load_data)
    ]
