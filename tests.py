from django.test import TestCase

# Create your tests here.
from xml.etree import ElementTree as ET
from xml.dom import minidom


def test_Sitemap(TestCase):
    def startUp(self):
	from django.contrib.sites.models import Site
	self.base_url = ''.join(['http://', Site.objects.get(pk=1).domain])
	self.base_images_urll = '/media'

    def test_SitemapCreate(self):
	sitemap = Sitemap()
	blog = sitemap.add_url('blog', self.base_url)
	image = sitemap.add_image(blog, '1_4.jpg', self.base_images_url)
	s = ET.tostring(sitemap.xml, encoding="utf-8", xml_declaration=True)
	self.assertIsInstance(s, str, 'ET.tostring executed on sitemap.xml return string')
	print '%s' % s
