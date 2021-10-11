from django.shortcuts import render, redirect
import os
import folium
# Create your views here.
def home(request):
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')

    m = folium.Map(location=[23.07,80.09], zoom_start=5)

    style_admin={'fillcolor':'#228B22','color' : '228B22'}
   

    folium.GeoJson(os.path.join(shp_dir,'admin.geojson'),name='admin',
      style_function=lambda x:style_admin).add_to(m)


    folium.LayerControl().add_to(m)


    m = m._repr_html_()


    context = {'my_map': m}
    return render(request, 'geoApp/home.html',context)
