<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="media\rms.png" alt="Project logo"></a>
</p>

# <div align= "center"> Restaurant Management System</div>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)]()
</div>

---

<p align="center"> A mini-web based project
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Authors](#authors)
- [Quick Preview](#preview)

<br>

## 🧐 About <a name = "about"></a>
This is an admin based  mini web project developed for the management of the records of food, billing and food sales. It is created with the motive of creating ease for the counter-management side of a restaurant.


<br>


## ✨ Features <a name = "features"></a>

### For Registered Users :

- Admin Mode
   - Admin can register new staff.
   - Admin can CREATE, RETRIVE, UPDATE and DELETE food items.
   - Admin can CREATE, RETRIVE, UPDATE, PRINT and DELETE    invoices.

<br>

- Staff Mode
   - Staff can CREATE, RETRIVE, UPDATE and DELETE food items.
   - Staff can CREATE, RETRIVE, UPDATE and PRINT invoices.
     
<br>

### For Unregistered users :
- Normal mode:
   - Can only view food-items list and food details.


<br>

## 🏁 Getting Started <a name = "getting_started"></a>

- Clone the repository or download the zip file

- For zip file extract it, then cd into the directory 

- make virtualenv and install the packages into the environment by:

    ```
    $ virtualenv venv

    $ venv\Scripts\activate (in windows) or $source venv/bin/activate (in Mac OS/linux)

    ```

- Install all dependencies by executing the following command:

    ```
    $pip install -r requirements.txt
    ```

- For running the application simply execute the following commands:

    ```
    $python manage.py migrate
    $python manage.py runserver
    ```

- For creating a user execute:

    ```
    $python3 manage.py createsuperuser
    # Follow the instructions
    ```

- You can now login to the system!

- Now you can use the app by visiting [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

<br>

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com) - Web Framework
- [Sqlite](https://www.sqlite.com/) - Database

<br>

## ✍️ Authors <a name = "authors"></a>

- [@MishanKhatri](https://github.com/Mishankhatri)
- [@Kushal_pangeni](https://github.com/Kushal213)

<br>

## 👀 Quick Preview <a name = "preview"></a>

 - Homepage 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\1.HomePage.png" alt="Home Page"></a>
</p>

 - Foodlist 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\2.Foodlist(admin).png" alt="Home Page"></a>
</p>

 - FoodInfo 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\3.Foodinfo(admin).png" alt="Home Page"></a>
</p>

 - Create Invoice 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\4.CreateInvoice.png" alt="Home Page"></a>
</p>

 - Add Items to Invoice
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\5.AddItemsToInvoice.png" alt="Home Page"></a>
</p>

 - Added Items Preview 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\6.ItemsAddedToInvoice.png" alt="Home Page"></a>
</p>

 - Print Invoice as Pdf 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\7.PrintInvoicePdf.png" alt="Home Page"></a>
</p>

 - Dashboard For Admin 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\8.DashboardAdmin.png" alt="Home Page"></a>
</p>

 - Update Profile
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\9.UpdateProfile.png" alt="Home Page"></a>
</p>

 - Add Food to Database 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\10.AddNewFoodItem.png" alt="Home Page"></a>
</p>

 - Register New Staff (admin only view)
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\11.RegisterNewStaff(adminonly).png" alt="Home Page"></a>
</p>

 - Sales(admin only view) 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\12.Sales(adminonly).png" alt="Home Page"></a>
</p>

 - Particular Invoice Details
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\13.InvoiceDetails.png" alt="Home Page"></a>
</p>

 - Deletion of Invoice (admin only) 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\14.DeletionOfInvoice(adminonly).png" alt="Home Page"></a>
</p>

 - Staff Dashboard 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\15.Staff-dashboard(no register of new staff tab).png" alt="Home Page"></a>
</p>

 - Staff Sales View 
<p align="">
 <img width=auto height=auto src="media\GithubPreviewPages\16.Staff-Salesview.png" alt="Home Page"></a>
</p>



