# Generated by Django 5.1.3 on 2024-12-04 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_bookinstance_borrower"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "ordering": ["due_back"],
                "permissions": (("can_mark_returned", "Set book as returned"),),
            },
        ),
    ]
