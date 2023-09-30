import datetime
from datetime import date, timedelta
from typing import Any

from django.contrib import messages
from django.db.models import Model
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import TipoInvestimento
