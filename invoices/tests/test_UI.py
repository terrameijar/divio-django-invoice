from django.test import LiveServerTestCase
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


class TestInvoicingApp(StaticLiveServerTestCase):

    def setUp(self):
        self.base_url = self.live_server_url
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver') # Add chrome driver to sys PATH first

    def test_landing_page_load(self):
        self.driver.get(self.base_url)
        self.assertEqual(self.driver.title, "Invoicing App")

    def test_new_invoice_can_be_created(self):
        self.driver.get(self.base_url)
        invoices_link = self.driver.find_element_by_id("invoices-dropdown")
        invoices_link.click()




    def tearDown(self):
        self.driver.quit()




