from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem

from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp

from helpers import screen_helper
import DatabaseHandlers

Window.size = (300,500) #remove when publishing app

class YearlyReportApp(MDApp):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transactions = DatabaseHandlers.get_sheet_from_database('Jaarlijkse begroting 2022', 'Transacties')
        self.options = DatabaseHandlers.get_sheet_from_database('Jaarlijkse begroting 2022', 'Opties')
        self.categories = DatabaseHandlers.get_categories(self.options, 1)

        self.screen = Builder.load_string(screen_helper)
        self.categorymenu = MDDropdownMenu()
        self.subcategorymenu = MDDropdownMenu()

    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.theme_style = 'Dark'
        self.screen = Builder.load_string(screen_helper)

        return self.screen

    def navigation_draw(self):
        print('navigation')

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.date_on_save)
        date_dialog.open()

    def date_on_save(self, instance ,value, date_range):
        global date_chosen
        date_chosen = str(value)
        self.root.ids.date_label.text = str(value)

    def refresh_transactionmenu(self):
        self.transaction_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Uitgave",
                "height": dp(56),
                "on_release":
                    lambda x=f"Uitgave": self.set_transactiontype(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": f"Inkomst",
                "height": dp(56),
                "on_release":
                    lambda x=f"Inkomst": self.set_transactiontype(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": f"Niet-Uitgave",
                "height": dp(56),
                "on_release":
                    lambda x=f"Niet-Uitgave": self.set_transactiontype(x)
            }
        ]
        self.transactionmenu = MDDropdownMenu(
            caller=self.screen.ids.transaction_type,
            items=self.transaction_items,
            position="center",
            width_mult=4,

        )
        self.categorymenu.bind()

    def refresh_categorymenu(self):
        self.categories_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{self.categories[i]}",
                "height": dp(56),
                "on_release":
                    lambda x=f"{self.categories[i]}": self.set_category(x)
            } for i in range(len(self.categories))
        ]
        self.categorymenu = MDDropdownMenu(
            caller=self.screen.ids.category_item,
            items=self.categories_items,
            position="center",
            width_mult=4,

        )
        self.categorymenu.bind()

    def set_category(self, chosen_category):
        global category_chosen
        self.screen.ids.category_item.set_item(chosen_category)
        category_chosen = chosen_category
        self.subcategories = DatabaseHandlers.get_subcategories(self.options, chosen_category)
        self.subcategories_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{self.subcategories[i]}",
                "height": dp(56),
                "on_release":
                    lambda x=f"{self.subcategories[i]}": self.set_subcategory(x)
            } for i in range(len(self.subcategories))
        ]
        self.subcategorymenu = MDDropdownMenu(
            caller=self.screen.ids.subcategory_item,
            items=self.subcategories_items,
            position="center",
            width_mult=4,

        )
        self.subcategorymenu.bind()
        self.categorymenu.dismiss()

    def set_subcategory(self, chosen_subcategory):
        global subcategory_chosen
        subcategory_chosen = chosen_subcategory
        self.screen.ids.subcategory_item.set_item(chosen_subcategory)
        self.subcategorymenu.dismiss()

    def set_transactiontype(self, chosen_transactiontype):
        global transaction_type_chosen
        transaction_type_chosen = chosen_transactiontype
        self.screen.ids.transaction_type.set_item(chosen_transactiontype)
        self.transactionmenu.dismiss()

    def add_transaction(self):
        amount_chosen = self.screen.ids.amount.text
        description_chosen = self.screen.ids.description.text
        DatabaseHandlers.insert_new_transaction(self.transactions,transaction_type_chosen, date_chosen, amount_chosen, description_chosen, category_chosen, subcategory_chosen)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    YearlyReportApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
