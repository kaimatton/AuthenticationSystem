import pyrebase
import customtkinter

# INITIALIZING FIREBASE
key = {
    'apiKey': "AIzaSyABVLqua83wVbSiEMcpAV6xljLsQlRSvus",
    'authDomain': "loginprojectpy.firebaseapp.com",
    'projectId': "loginprojectpy",
    'storageBucket': "loginprojectpy.appspot.com",
    'messagingSenderId': "710753956546",
    'appId': "1:710753956546:web:14b5d81c710e342c5ec15b",
    'measurementId': "G-8WQEYBM6VV",
    'databaseURL': ''
}
config = key
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# BACK END FOR SIGN IN
    # Gets Email Input
def userLogin_clicked(event):
    if userLogin.get() == 'Enter UserName':
        userLogin.delete(0, customtkinter.END)
        userCreate.insert(0, '')

    # Gets Password Inout
def passwordLogin_clicked(event):
    if passwordLogin.get() == "Enter Password":
        passwordLogin.delete(0, customtkinter.END)
        passwordLogin.insert(0,'')
    # Hides or Shows Password
def passwordShow():
    if var.get() == 1:
        passwordLogin.configure(show='')
    else:
        passwordLogin.configure(show='*')
    # Signs In User
 
def login():
    try:
        email = userLogin.get()
        password = passwordLogin.get()
        SignIn_Auth = auth.sign_in_with_email_and_password(email, password)
        if SignIn_Auth:
                active = customtkinter.CTkFrame(app,
                                         width = 400,
                                         height = 450,
                                         corner_radius = 30                                        
                )
                active.place(relx=.5, rely=.5, anchor=customtkinter.CENTER)

                signedInSuccess = customtkinter.CTkLabel(app,
                                                    height= 55,
                                                    text ="Login Success",                                   
                                                    text_color = 'green',
                                                    bg_color = 'lightgreen',
                )
                signedInSuccess.configure(font=('Helvetica',32))
                signedInSuccess.place(relx=.5,rely=.20, anchor=customtkinter.CENTER)
                

    except Exception:
                signedInFail = customtkinter.CTkLabel(app,
                                                    height= 55,
                                                    text ="Login Failed",                                   
                                                    text_color = 'red',
                                                    bg_color = 'pink',
                )
                signedInFail.configure(font=('Helvetica',32))
                signedInFail.place(relx=.5,rely=.20, anchor=customtkinter.CENTER)

                signedInFail2 = customtkinter.CTkLabel(app,
                                                    height= 55,
                                                    text ="Please Enter Valid Email or Password",                                   
                                                    text_color = 'red',
                                                    bg_color = 'grey90',
                )
                signedInFail2.configure(font=('Helvetica',14))
                signedInFail2.place(relx=.5,rely=.45, anchor=customtkinter.CENTER)


# BACK END FOR SIGN UP 
    # Creates User
def createUser_clicked(event):
    if userCreate.get() == 'Enter Valid Email':
        userCreate.delete(0,customtkinter.END)
        userCreate.insert(0, '')

    # Creates password
def createPassword_clicked(event):
    if passwordCreate.get() == 'Enter Valid Email':
        passwordCreate.delete(0, customtkinter.END)
        passwordCreate.insert(0, '')

    # Creates Account
def create():
    try:
        email = userCreate.get()
        password = passwordCreate.get()
        user = auth.create_user_with_email_and_password(email, password)
        createSucess = customtkinter.CTkLabel(app,
                                                    height= 15,
                                                    text ="Account Created",                                   
                                                    text_color = 'green',
                                                    bg_color = 'light green',
                )
        createSucess.configure(font=('Helvetica',12))
        createSucess.place(relx=.5,rely=75, anchor=customtkinter.CENTER)
    except Exception:
                createFail = customtkinter.CTkLabel(app,
                                                    height= 55,
                                                    text ="Email Already Exists or Error",                                   
                                                    text_color = 'red',
                                                    bg_color = 'grey90',
                )
                createFail.configure(font=('Helvetica',14))
                createFail.place(relx=.5,rely=.45, anchor=customtkinter.CENTER)

'''
DEFAULT SETTING FOR FRONT END
'''
# Default Appearence 
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')

# App start 
app = customtkinter.CTk()
app.geometry('500x500')
app.title("Sign In")
  
'''
Sign Up Page Front End
'''
def signupPage(): 
    global createAccButton
    global returnLoginFrame
    global userCreate
    global passwordCreate

    # When 'return to sign in' is clicked, destroys everything in SignupPage
    def returnMain():
        signupFrame.destroy()
        userCreate.destroy()
        passwordCreate.destroy()
        frameText1.destroy()
        frameText2.destroy()
        returnLoginFrame.destroy()
        createAccButton.destroy()

# Sign up Frame
    signupFrame = customtkinter.CTkFrame(app,
                                         width = 400,
                                         height = 450,
                                         corner_radius = 30                                        
)
    signupFrame.place(relx=.5, rely=.5, anchor=customtkinter.CENTER)

# Sign up Entries
    userCreate = customtkinter.CTkEntry(app,
                                width = 300,
                                height = 40,
                                corner_radius = 30,
                                justify = 'center',
                                bg_color= 'grey90',
                                placeholder_text= 'Enter Email',
                                placeholder_text_color = 'black',
                                border_color = 'black',
    )
    userCreate.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)
    userCreate.bind('<FocusIn>', createUser_clicked)

    passwordCreate = customtkinter.CTkEntry(app,
                                            width = 300,
                                            height = 40,
                                            corner_radius = 30,
                                            justify = 'center',
                                            bg_color= 'grey90',
                                            placeholder_text= 'Create a password',
                                            placeholder_text_color = 'black',
                                            border_color = 'black',
    )
    passwordCreate.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
    passwordCreate.bind('<FocusIn>', createPassword_clicked)

# Signup Buttons
    returnLoginFrame = customtkinter.CTkButton(app,
                                      width = 80,
                                      height = 15,
                                      text = 'Return to Sign in Page',
                                      text_color = 'white',
                                      border_color = 'black',
                                      corner_radius = 30,
                                      bg_color = 'grey90',
                                      command = returnMain
    )
    returnLoginFrame.place(relx=0.5, rely=0.92, anchor=customtkinter.CENTER)

    createAccButton = customtkinter.CTkButton(app,
                                      width = 200,
                                      height = 30,
                                      text = 'Create Account',
                                      text_color = 'white',
                                      border_color = 'black',
                                      corner_radius = 30,
                                      bg_color = 'grey90',
                                      command= create
    )
    createAccButton.place(relx=0.5, rely=0.70, anchor=customtkinter.CENTER)

# Signup Text Labels
    frameText1 = customtkinter.CTkLabel(app,
                                   height= 25,
                                   text ="Sign Up",                                   
                                   text_color = 'black',
                                   bg_color = 'grey90'
    )
    frameText1.configure(font=('Helvetica',32))
    frameText1.place(relx=.5,rely=.20, anchor=customtkinter.CENTER )

    frameText2 = customtkinter.CTkLabel(app,
                                   height= 20,
                                   text = "Please use an Existing Email",                                   
                                   text_color = 'red',
                                   bg_color = 'grey90'
    )
    frameText2.configure(font=('Helvetica',12))
    frameText2.place(relx=.5,rely=.42, anchor=customtkinter.CENTER )

'''
LOGIN PAGE 
'''
# Login Frame
loginFrame = customtkinter.CTkFrame(app,
                                width = 400, 
                                height = 450,
                                corner_radius = 30,                                
)
loginFrame.place(relx=.5, rely=.5, anchor=customtkinter.CENTER)

# Login Entries
userLogin = customtkinter.CTkEntry(app,
                                width = 300,
                                height = 40,
                                corner_radius = 30,
                                justify = 'center',
                                bg_color= 'grey90',
                                placeholder_text= 'Enter UserName',
                                placeholder_text_color = 'dodger blue',
                                border_color = 'black'
)
userLogin.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)
userLogin.bind('<FocusIn>', userLogin_clicked)

passwordLogin = customtkinter.CTkEntry(app,
                                      width = 300,
                                      height = 40, 
                                      corner_radius = 30, 
                                      justify = 'center',
                                      bg_color = 'grey90',
                                      placeholder_text = 'Enter Password', show = '*',
                                      placeholder_text_color = 'dodger blue',
                                      border_color = 'black'
)
passwordLogin.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
passwordLogin.bind('<FocusIn>', passwordLogin_clicked)


# Sign In Buttons
loginButton = customtkinter.CTkButton(app,
                                      width = 200,
                                      height = 30,
                                      text = 'Login',
                                      text_color = 'white',
                                      border_color = 'black',
                                      corner_radius = 30,
                                      bg_color = 'grey90',
                                      command = login
)
loginButton.place(relx=0.5, rely=0.70, anchor=customtkinter.CENTER)

signUpButton = customtkinter.CTkButton(app,
                                      width = 80,
                                      height = 15,
                                      text = 'Create an Account',
                                      text_color = 'white',
                                      border_color = 'black',
                                      corner_radius = 30,
                                      bg_color = 'grey90',
                                      command = signupPage
)
signUpButton.place(relx=0.5, rely=0.92, anchor=customtkinter.CENTER)

# Sign In Label Text 
frameText = customtkinter.CTkLabel(app,
                                   height= 55,
                                   text ="Sign In",                                   
                                   text_color = 'black',
                                   bg_color = 'grey90'
)
frameText.configure(font=('Helvetica',32))
frameText.place(relx=.5,rely=.20, anchor=customtkinter.CENTER )

# check boxes
var = customtkinter.IntVar() 
passwordShow = customtkinter.CTkCheckBox(app,
                                      width=10,
                                      height=10,
                                      text="Show Password",
                                      text_color = 'dodger blue',
                                      checkbox_height= 12,
                                      checkbox_width=12,
                                      font=('Arial', 12),
                                      bg_color='gray90',
                                      command = passwordShow,
                                      variable = var  
)
passwordShow.place(relx=0.5, rely=0.63, anchor=customtkinter.CENTER)
'''
SIGN IN SUCCESSFUL PAGE
'''
app.mainloop()