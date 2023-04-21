setup = {'drive': 'C:\\PythonSelenium\\drivers\\chromedriver.exe',
          'url' : 'http://10.1.33.16/'
        }
chart_login = {'username' : '//*[@id="Username"]',
               'password' : '//*[@id="Password"]',
               'click_login' : '//*[@id="login-div"]/div[3]/div/input',
               'click_chart' : '/html/body/ul/li[6]/a',
               'welcome' : '//*[@id="form1"]/ul/li[1]/a'
                }

chart_login_data = {'username' : 'Gururaj',
                    'password' : 'Gururaj!123'
                    }

chart_select = {'select_test_type' : '//*[@id="DDTest"]',
                'select_batch' : '//*[@id="DDBatch"]',
                'select_chart' : '//*[@id="DDChartType"]',
                'select_dimension' : '//*[@id="DDDimension"]',
                'click_generate_chart' : '//*[@id="GenerateChartBtn"]',
                'click_details': '//input[@id="DetailBtn"]',
                'select_attempts' : '//*[@id="DDAttempts"]/option',
                'click_download_chart' : '//input[@id="SaveBtn"]',
                'generate_popup' : '//*[@id="lblModalValue"]',
                'download_popup' : '//*[@id="lblModalValue"]',
                'click_close_generate' : '//*[@id="myModal"]/div/div/div[3]/button',
                'click_close_download' : '//*[@id="myModal"]/div/div/div[3]/button',
                'chart_cloumn_popup' : '//span[@id="lblModalValue"]',
                'chart_colunm_click' : '//*[@id="myModal"]/div/div/div[3]/button',
                'chart_column_error' : 'lblModalValue',
                'chart_column_error_close' : '//*[@id="myModal"]/div/div/div[3]/button'

                }

###################Admin login################################
SCROLL = {'SCROLL': "window.scrollTo(0,document.body.scrollHeight)"}

ADMINLOGINDATA = {'USERNAME': 'Gururaj',
                  'PASSWORD': 'Gururaj!123',
                  'WUSERNAME': 'GURU',
                  'WPASSWORD': 'GURU123'}

AddInfo={ 'AddEmp' : "//*[@id='addBtn']",

          "BasicInfo" : "//*[@id='hideDiv']/form/div/div/ul/li[1]/a",
          'BasicInfo_EmpNo' : "//*[@id='empNo']",
          "BasicInfo_EmpName" : "//*[@id='empName']",
          "BasicInfo_Batch" : "//*[@id='batch']",
          "BasicInfo_DOJ" : "//*[@id='doj']",
          "BasicInfo_Location" : "//*[@id='basicInfo']/div[2]/div[2]/select",
          "BasicInfo_Status" : "//*[@id='basicInfo']/div[2]/div[3]/select",
          "BasicInfo_EQ" : "//*[@id='educational_qualification']",
          "BasicInfo_Branch" : "//*[@id='Branch']",

          "Training_info" : "//*[@id='hideDiv']/form/div/div/ul/li[2]/a",
          "TrainingInfo_FCA_L_Prog" : "//*[@id='trainningInfo']/div[1]/div[1]/select",
          "TrainingInfo_FCA_L_Score":"//*[@id='FCA_L_PL_Score']",
          "TrainingInfo_FCA_L_PL_date":"//*[@id='FCA_L_PL_Date']",
          "TrainingInfo_TCB_Assigned":"//*[@id='trainningInfo']/div[3]/div[1]/div[1]/select",
          "TrainingInfo_TCB_Prog_Lang":"//*[@id='trainningInfo']/div[3]/div[1]/div[2]/select",
          "Training_TCB_Specialization" :"//*[@id='TCB_Specialization']",
          "TrainingInfo_Practice" :"//*[@id='trainningInfo']/div[3]/div[2]/div[1]/select",
          "Training_Stage":"//*[@id='trainningInfo']/div[3]/div[2]/div[2]/select",
          "Training_Stage2_StartDate":"//*[@id='Stage_2_Start']",
          "Training_Stage3_StartDate" :"//*[@id='Stage_3_Start']",
          "Training_Stage4_StartDate":"//*[@id='Stage_4_Start']",
          "FCA_SE_1":"//*[@id='FCA_SE_1']",
          "FCA_SE_2":"//*[@id='FCA_SE_2']",
          "FCA_SE_3":"//*[@id='FCA_SE_3']",
          "FCA_SE_cleareddate":"//*[@id='FCA_SE_Cleared_Date']",
          "SE_Attempts" :"//*[@id='SE_Attempts']",
          "PL_Training_date":"//*[@id='Prog_Lang_Training_Start']",
          "SCL_End_date":"//*[@id='SCL_End']",
          "FCA_PL1_score":"//*[@id='FCA_PL1']",
          "FCA_PL2_score":"//*[@id='FCA_PL2']",
          "FCA_PL3_score":"//*[@id='FCA_PL3']",
          "FCA_PL_Cleared_Date":"//*[@id='FCA_PL_Cleared_Date']",
          "PL_Attempts":"//*[@id='PL_Attempts']",
          "Prog_Lang_Trg_End":"//*[@id='Prog_Lang_Trg_End']",
          "trainningInfo_Hackathon1_feedback":"//*[@id='trainningInfo']/div[9]/div/div[1]/select",
          "trainningInfo_Hackathon2_feedback":"//*[@id='trainningInfo']/div[9]/div/div[2]/select",

          "Other_info":"//*[@id='hideDiv']/form/div/div/ul/li[3]/a",
          "Project_Start_Date":"//*[@id='Project_Start_Date']",
          "Other_info_Project":"//*[@id='Project']",
          "Other_info_KenMap_date1":"//*[@id='otherInfo']/div[2]/div[1]/input",
          "Other_info_KenMap_date2":"//*[@id='otherInfo']/div[2]/div[2]/input",
          "KenMap_rating":"//*[@id='otherInfo']/div[2]/div[3]/input",
          "Other_info_comments":"//*[@id='Comments']",
          "Other_info_Save":"//*[@id='otherInfo']/div[3]/div[2]/input",
}


ADMINLOGIN = {'USERNAME': '//*[@id="Username"]',
              'PASSWORD': '//*[@id="Password"]',
              'LOGIN': '//*[@id="login-div"]/div[3]/div/input',
              'DISPLAYTEXT': '/html/body/ul/li[2]/a',
              'INVALIDTEXT': '//*[@id="login-div"]/div[4]/label',
              'USERNAMEEXISTS':'/html/body/div/div/div[1]/form/div[1]/div/div[1]/div[1]/label[2]',
              'EMAILEXISTS':'/html/body/div/div/div[1]/form/div[1]/div/div[1]/div[4]/label[2]',
              'EDITSAVETEXT':'//*[@id="myModal"]/div/div/div[2]',
              'DELETETEXT':'//*[@id="deleteModal"]/div/div/div[2]'

              }
ADMIN = {'ADMINCLICK': '/html/body/ul/li[7]/a',
         'USERNAME': '//*[@id="Usernameid"]',
         'DISPLAYNAME': '//*[@id="DisplayName"]',
         'PASSWORD': '//*[@id="txtPassword"]',
         'PASSWORDVIEW':'//*[@id="togglePassword"]',
         'EMAIL': '//*[@id="Emaildisable"]',
         'DATAUPDATE': '//*[@id="Checkboxcount"]',
         'DATAVIEW': '//*[@id="Checkboxcount1"]',
         'ADMIN': '//*[@id="AdminCheckbox"]',
         'CANCEL': 'btn2',
         'CREATE': '//*[@id="btn"]',
         'EDIT':'//*[@id="webgrid"]/tbody/tr[1]/td[10]/a',
         'EDITSAVE':'//*[@id="btn1"]',
         'EDITCLOSE':'//*[@id="myModal"]/div/div/div[3]/button',
         'DELETE':'//*[@id="webgrid"]/tbody/tr[5]/td[11]/a',
         'DELETECLOSE':'//*[@id="deleteModal"]/div/div/div[3]/button',
         'DELETEINSIDE':'//*[@id="deleteLink"]'


         }
ADMINLOGINDATA = {'USERNAME': 'Gururaj',
                  'PASSWORD': 'Gururaj!123',
                  'WUSERNAME': 'GURU',
                  'WPASSWORD': 'GURU123'}

ADMINDATA={'USERNAME':'RAKSHITH2',
           'DISPLAYNAME':'RAKSHITH',
           'PASSWORD':'Rakshi@123',
           'EMAIL':'rakshith1234@gmail.com'}

############################################filemanager##############################################

FILEDATA={'FILEMANAGERCLICK':'/html/body/ul/li[3]/a',
          'FILESELECT':'//*[@id="summary"]/form/div[1]/select',
          'FILEBROWSER':'//*[@id="summary"]/form/div[2]/input',
          'SUBMIT':'//*[@id="summary"]/form/input',
          'TRACKERCLICK':'//*[@id="filemanagermenu"]/div[1]/div[1]/button[1]/a',
          'TCRCLICK':'//*[@id="filemanagermenu"]/div[1]/div[1]/button[2]/a'
          }


######################################data center#################################################

DATACENTRE={'DATACENTRECLICK':'/html/body/ul/li[4]/a',
            'DISPLAYTEXT':'/html/body/div/div/h2',
            'DOWNLOAD':'//*[@id="showDiv"]/div/a',
            'SEARCH':'//*[@id="key_search"]',
            'SEARCHCLICK':'//*[@id="showDiv"]/form[1]/p/input[2]',
            'EDIT':'//*[@id="GridId"]/table/tbody/tr[1]/td[42]/input',
            'DELETE':'//*[@id="GridId"]/table/tbody/tr[1]/td[43]/a',
            'DELETETEXT':'//*[@id="deleteConfModal"]/div/div/div[2]',
            'DELETECLOSE':'//*[@id="deleteConfModal"]/div/div/div[3]/button',
            'DELETEDELETE':'//*[@id="deleteLink"]'
}


DATACENTREINPUT={'NAME':'SURAJ',
                 'ID':'212928',
                 'BATCH':'1',
                 'LOCATION':'BENGALURU',
                 'DATE':'03-aug-2022',
                 'BRANCH':'ECE'}

DATACENTRE={'DATACENTRECLICK':'/html/body/ul/li[4]/a',
            'DISPLAYTEXT':'/html/body/div/div/h2',
            'DOWNLOAD':'//*[@id="showDiv"]/div/a',
            'SEARCH':'//*[@id="key_search"]',
            'SEARCHCLICK':'//*[@id="showDiv"]/form[1]/p/input[2]',
            'EDIT':'//*[@id="GridId"]/table/tbody/tr/td[42]/input',
            'DELETE':'//*[@id="GridId"]/table/tbody/tr/td[43]/a',
            'DELETETEXT':'//*[@id="deleteConfModal"]/div/div/div[2]',
            'DELETECLOSE':'//*[@id="deleteConfModal"]/div/div/div[3]/button',
            'DELETEDELETE':'//*[@id="deleteLink"]'

}


DATACENTREINPUT={'NAME':'Prateeksha',
                 'ID':'212733',
                 'BATCH':'2',
                 'LOCATION':'BENGALURU',
                 'DATE':'03-aug-2022',
                 'BRANCH':'ECE'}


CLICKDATA={
    'CLICK':'/html/body/ul/li[4]/a'
}
LOGIN= {
    'login' :'//*[@id="Username"]',
    'username':"Gururaj",
    'passwordtext':'//*[@id="Password"]',
    'password': "Gururaj!123",
    'loginbutton':'//*[@id="login-div"]/div[3]/div/input'

}
DICTIONARY = {
    'SEARCHCLEAR': "//*[@id='key_search']",
    'SEARCHAREA': "//*[@id='key_search']",
    'SEARCHSUBMIT' : "//*[@id='showDiv']/form[1]/p/input[2]",
    'EDIT' : "//*[@id='GridId']/table/tbody/tr/td[42]/input",
    'ELOCATION' : "//*[@id='basicInfo']/div[2]/div[2]/select" ,
    'EEDUDETAILS' : "//*[@id='educational_qualification']",
    'EBRANCH' : "//*[@id='Branch']",
    'clickBasicToTraining' : "//*[@id='basicInfo']/a",
    'EFcaPL' : "//*[@id='trainningInfo']/div[1]/div[1]/select",
    'EFca_L_PL_Score' : "//*[@id='FCA_L_PL_Score']",
    'ETcb_Assign' : "//*[@id='trainningInfo']/div[3]/div[1]/div[1]/select",
    'ETcb_prog_lang' :"//*[@id='trainningInfo']/div[3]/div[1]/div[2]/select",
    'EPRACTICE' : "//*[@id='trainningInfo']/div[3]/div[2]/div[1]/select",
    'Etraining_stage' : "//*[@id='trainningInfo']/div[3]/div[2]/div[2]/select",
    'EFCA_SE_1' : "//*[@id='FCA_SE_1']",
    'EFCA_SE_2': "//*[@id='FCA_SE_2']",
    'EFCA_SE_3': "//*[@id='FCA_SE_3']",
    'ESe_attempts': "//*[@id='FCA_SE_3']",
    'EFCA_PL1_Score': "//*[@id='FCA_PL1']",
    'EFCA_PL2_Score': "//*[@id='FCA_PL2']",
    'EFCA_PL3_Score': "//*[@id='FCA_PL3']",
    'EPL_attempts' : "//*[@id='PL_Attempts']",
    'EHACK1':"//*[@id='trainningInfo']/div[9]/div/div[1]/select",
    'EHACK2': "//*[@id='trainningInfo']/div[9]/div/div[2]/select",
    'EclickBasicToOtherInfo': "//*[@id='trainningInfo']/a[2]",
    'EProjectName': "//*[@id='Project']",
    'EKenMap2': "//*[@id='otherInfo']/div[2]/div[2]/input",
    'ECOMMENTS':"//*[@id='Comments']",
    'SAVEBUTTON':"//*[@id='otherInfo']/div[3]/div[2]/input",
    'CANCLEEDIT': "//*[@id='otherInfo']/div[3]/div[2]/a[2]"
}

DICTINPUT= {
    'SEARCHSAVE': "Shivali",
    'IPLOCATION': "Bengaluru",
    'IPEDUDETAILS' : "Masters",
    'IPBRANCH' : "AI & ML",
    'IPFcaPL' : "C#",
    'IPFca_L_PL_Score' : '40',
    'IPTcb_Assign' : '.Net',
    'IPTcb_prog_lang' :"JavaScript",
    'IPPRACTICE' : "System Software",
    'IPtraining_stage': "2",
    'IPFCA_SE_1' : '30',
    'IPFCA_SE_2' : '40',
    'IPFCA_SE_3' : '70',
    'IPSe_attempts': '3',
    'IPFCA_PL1_Score': '40',
    'IPFCA_PL2_Score': '45',
    'IPFCA_PL3_Score': '80',
    'IPPL_attempts': '3',
    'IPHACK1': "Average",
'IPHACK2': "Average",
    'IPProjectName' : "Web application Development",
    'IPKenMap2':"12/01/2023",
    'IPCOMMENTS': "Well done!! Keep working hard",
    'IPCANCEL' : 'Bhavana',
    'IPEDITID' : '212733',
    'IPEDITID1' : '212334'

}