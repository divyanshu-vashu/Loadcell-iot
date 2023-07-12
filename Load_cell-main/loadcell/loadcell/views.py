# import matplotlib
# matplotlib.use("Agg")  # Use the backend that does not require an X server
# import matplotlib.pyplot as plt
# import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# import os

def generate_graph(request):
    return render(request, 'index.html')