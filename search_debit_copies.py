'''
Created on 19-Jul-2020

@author: Gowtham Lakshman
'''
from _winapi import TerminateProcess
from future.backports.test.ssl_servers import threading

'''
Created on Jul 8, 2020

@author: glakshmanan2
'''

import os
import re
import datetime
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
import threading 
import sys




def file_read(fname,content_array,dcs):
        
        if (dcs=="Customer Complaints" or dcs=="EL Copies"):
            db_cpy_len = 8
        else:
            db_cpy_len = 6
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                
                for line in f:
                    content_array.append(line[:db_cpy_len])
         
                


def search_string_in_file(file_name, string_to_search, path_a,dcs):
    
    if dcs=="Customer Complaints":
        search_string_in_file_cc(file_name, string_to_search, path_a)
        
    if (dcs=="EL Copies" or dcs=="Multisaver" or dcs=="Coupon"):
        search_string_in_file_el(file_name, string_to_search, path_a)
    
    if dcs=="VATPPD":    
        search_string_in_file_vatppd(file_name, string_to_search, path_a)
    
def search_string_in_file_cc(file_name, string_to_search, path_a):

    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    final_list = []
    
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            list_of_results.append(line)
            
            #print(string_to_search, line)
           
            result = re.search(string_to_search, line)
                                               
            if result:
#               print(line_number," ",file_name," ",string_to_search," ",line)
                final_list.append(list_of_results[line_number-1])
                
                var1=line_number-2 
                
                
                
                for var in list_of_results:
                    
                    str1=list_of_results[var1]
                    
                    if str1[:2] == "01":
                        final_list.append(list_of_results[var1])
                        
                    else:
                        break
                    
                    var1 = var1 - 1
                
                final_list.reverse()
                
                
    write_file_para(path_a, final_list)
                           
def search_string_in_file_el(file_name, string_to_search, path_a):

    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    #line_number = -1
    list_of_results = []
    final_list = []
    print_flag=0
    print_flag_a=0
    
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        #for line in read_obj:
            # For each line, check if line contains the string
        #    list_of_results.append(line)
            
            #print(string_to_search, line)
        for srch_var in read_obj:
            #line_number += 1
            result = re.search(string_to_search, srch_var)
                                               
            if result:
#               print(line_number," ",file_name," ",string_to_search," ",line)
                final_list.append(srch_var)
                print_flag=1
                
                
            if (print_flag==1 and srch_var[:1]!="0"):    
                final_list.append(srch_var)
                print_flag_a=1
            
            if (print_flag_a==1 and srch_var[:1]=="0"):    
                break
                
                #final_list.reverse()
                
                
    write_file_para(path_a, final_list)            
                
                
def search_string_in_file_vatppd(file_name, string_to_search, path_a):

    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    #line_number = 0
    list_of_results = []
    final_list = []
    
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            
            #list_of_results.append(line)
            
            #print(string_to_search, line)
        
            result = re.search(string_to_search, line)
                                               
            if result:
#               print(line_number," ",file_name," ",string_to_search," ",line)
                final_list.append(line)
                
                #var1=line_number+1
                
                
                #final_list.reverse()
                
                
    write_file_para(path_a, final_list)                          
             
                
def write_file_para(path_a, final_list):                
    f = open(path_a, "a")
           
    for var2 in final_list:
        f.write(var2)
    
    f.close()                
                
def run_msg(final_out_msg):
    
    msg.delete(0,END)
    msg.insert(0,final_out_msg) 
    exit()




def process_para():
    
    dtv = datetime.datetime.now()
        
    d=dtv.strftime("%d")
    m=dtv.strftime("%m")
    y=dtv.strftime("%Y")
    hh=dtv.strftime("%H")
    mm=dtv.strftime("%M")
    ss=dtv.strftime("%S")
    
    dcs=dc_select.get()
    
    
    op=out_path.get()
    
    slash="\ "
    
    if dcs=="EL Copies":
        dcs_fp="EL"
    else:
        dcs_fp=dcs
    
    
    path_a = op + slash[:1] + dcs_fp + " Copies "+ d + m + y + hh + mm + ss + ".txt"
    
    path=inp1.get()
    
    Srch_file=inp2.get()
    
    p = path + "\ "
    
    
    if(validate_para(op,path,Srch_file,dcs))==1:
        threading.Thread(target=process_para_1,args=(path, Srch_file,path_a, p,dcs, )).start()
    
    


def validate_para(op,path,Srch_file,dcs):
    
    ok_flag=0
        
    if(os.path.isfile(Srch_file) and os.path.isdir(path) and os.path.isdir(op) and dcs!=""):
        ok_flag=1
        
    
    if ok_flag==0:
        
        out_msg="Please check your entry.. "
        threading.Thread(target=run_msg,args=(out_msg,)).start()    
    
    return ok_flag    

def process_para_1(path, Srch_file,path_a, p, dcs):        
    
    
    
    
    file_dir = []
        
   
 
    for file in os.listdir(path):
           
        file_dir.append( p[:len(p)-1]  + file)
    
   

    content_array = []           


    file_read(Srch_file,content_array, dcs)                

    no = 1 
    for x in content_array:
        out_msg="Running Please wait.. Debit # in progress " + x + " which is " + str(no) + " of " + str(len(content_array))
        threading.Thread(target=run_msg,args=(out_msg,)).start()
    
        for y in file_dir:
            search_string_in_file(y,x,path_a,dcs)
            
        no += 1
    
    out_msg="Please check the file @ "+path_a  
    threading.Thread(target=run_msg,args=(out_msg,)).start()
    
    exit()
        
    
        
    
#----------------------------Main program starts here-----------------------------------------  


main = Tk()
main.title("Debit Copies Extraction Utility") 
main.geometry("900x350")

Label(main, text = "Enter files in folder path: \n", font=("calibri", 16)).grid(row=0)

Label(main, text = "Enter the file with debit # : \n",font=("calibri", 16)).grid(row=1)

Label(main, text = "Place Output file in : \n",font=("calibri", 16)).grid(row=2)

Label(main, text = "Select Debit Note Type : \n",font = ("calibri", 16)).grid(row = 3)

Label(main, text = "Message :\n",font=("calibri", 16)).grid(row=4)


  
dc_select = StringVar() 
dc_list = Combobox(main, textvariable = dc_select) 
  
# Adding combobox drop down list 
dc_list['values'] = ('Customer Complaints',  
                    'EL Copies', 
                    'Multisaver', 
                    'Coupon',
                    'VATPPD') 
  
dc_list.grid(row=3, column = 1, ipadx=190)


inp1 = Entry(main)

inp2 = Entry(main)

out_path = Entry(main)

msg = Entry(main)

inp1.grid(row=0, column=1,ipadx=200)
inp2.grid(row=1, column=1,ipadx=200)
out_path.grid(row=2, column=1,ipadx=200)
msg.grid(row=4,column=1,ipadx=200)



Button(main, text='Cancel', command=main.destroy).grid(row=5, column=2)
Button(main, text='Run', command=process_para).grid(row=5, column=0)

mainloop()
