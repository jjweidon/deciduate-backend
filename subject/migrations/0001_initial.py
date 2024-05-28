import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("major", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassOf",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(verbose_name="학년")),
            ],
            options={
                "db_table": "class_of",
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "area",
                    models.CharField(
                        choices=[("M", "전공"), ("L", "교양")],
                        max_length=2,
                        verbose_name="개설영역",
                    ),
                ),
                ("grade", models.IntegerField(null=True, verbose_name="학년")),
                ("name", models.CharField(max_length=100, verbose_name="과목명")),
                ("credit", models.IntegerField(verbose_name="학점")),
            ],
            options={
                "db_table": "subject",
            },
        ),
        migrations.CreateModel(
            name="MajorCompulsory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "main_compulsory",
                    models.BooleanField(default=True, verbose_name="본전공 필수"),
                ),
                (
                    "sub_compulsory",
                    models.BooleanField(default=True, verbose_name="이중/부전공 필수"),
                ),
                (
                    "class_of",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="class_of_major_compulsories",
                        to="subject.classof",
                        verbose_name="학번",
                    ),
                ),
                (
                    "major",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="major",
                        to="major.major",
                        verbose_name="전공",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subject_major_compulsory",
                        to="subject.subject",
                        verbose_name="과목",
                    ),
                ),
            ],
            options={
                "db_table": "major_compulsory",
            },
        ),
        migrations.CreateModel(
            name="LiberalCompulsory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(max_length=20, null=True, verbose_name="교양 영역"),
                ),
                ("compulsory", models.BooleanField(default=True, verbose_name="교양 필수")),
                (
                    "class_of",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="class_of_liberal_compulsories",
                        to="subject.classof",
                        verbose_name="학번",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subject_liberal_compulsory",
                        to="subject.subject",
                        verbose_name="과목",
                    ),
                ),
            ],
            options={
                "db_table": "liberal_compulsory",
            },
        ),
    ]
