screen_helper = """

Screen:
    category_item: category_item.__self__
    
        
    MDToolbar:
        id: toolbar
        title: 'Finances 2022'
        pos_hint: {'top':1.0}
        left_action_items: [["menu", lambda x:app.navigation_draw() ]]
        elevation: 8
   
    MDLabel:
            
    MDRectangleFlatButton:
        id: date_label
        text: 'Choose date'
        pos_hint: {'center_x': 0.5, 'top': 0.8}
        on_release: app.show_date_picker()   
    
    MDTextField: 
        id: amount
        hint_text: "Enter Amount (€)"
        icon_right : "cash-multiple"
        icon_right_color: app.theme_cls.primary_color
        valign:'center'
        pos_hint: {'center_x': 0.5, 'top': 0.7}
        size_hint_x: None
            
    MDTextField: 
        id: description
        hint_text: "Enter description"
        icon_right : "android"
        icon_right_color: app.theme_cls.primary_color
        valign:'center'
        pos_hint: {'center_x': 0.5, 'top': 0.6}
        size_hint_x: None
            
    MDDropDownItem:
        id: transaction_type   
        pos_hint: {'center_x': 0.5, 'top': 0.5}
        text:'Choose transaction type'
        on_release: 
            app.refresh_transactionmenu()
            app.transactionmenu.open()
    
    MDDropDownItem:
        id: category_item   
        pos_hint: {'center_x': 0.5, 'top': 0.4}
        text:'Choose category'
        on_release: 
            app.refresh_categorymenu()
            app.categorymenu.open()
      
    MDDropDownItem:
        id: subcategory_item  
        pos_hint: {'center_x': 0.5, 'top': 0.3}
        text:'Choose subcategory'
        on_release: 
            app.subcategorymenu.open()
            
    MDRectangleFlatButton:
        id: add_transaction
        text: 'Add Transaction'
        pos_hint: {'center_x': 0.5, 'top': 0.2}
        on_release: app.add_transaction()   


"""