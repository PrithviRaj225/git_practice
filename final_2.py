from kite_trade import *
import pdb
import datetime
import time
import pandas as pd

from datetime import date
from datetime import timedelta
import pywhatkit
import requests

import pyotp



#G5DJLRNVHWVZPOH3EZZIBY622XBWX433
totp = pyotp.TOTP('VEH5HP6DRQJWEJPPKK3TJYKC4L6B27MI')
totp = totp.now() 

user_id = "CR3647"       # Login Id
password = "sumipruthvi17"      # Login password
twofa = totp         # Login Pin or TOTP

enctoken = get_enctoken(user_id, password, twofa)
kite = KiteApp(enctoken=enctoken)
#enctoken = "BteDGtog0QdViEeryhw2/Ga96TQ2T9KTLjKG3ZJfHi2jh3XgwN/MNaZVHGZ8cfoMVMwUr/me5YDxgUbhRUyQoQ67wUBMjMS1088hQWjDQmGrf5zEarA2MA=="



#fuction 
ce_filename = str(datetime.datetime.now().date()) + ' CE00' + '.txt'
pe_filename = str(datetime.datetime.now().date()) + ' PE00' + '.txt'
ce_avg = str(datetime.datetime.now().date()) + ' CE2' + '.txt'
pe_avg = str(datetime.datetime.now().date()) + ' PE2' + '.txt'


step_values = {'NIFTY':100,'BANKNIFTY':100 , "SENSEX":100, "FINNIFTY":100 , "BANKEX":100}

def get_data(name,segment,delta,interval,continuos):
    token = kite.ltp([segment + name])[segment + name]['instrument_token']
    to_date = datetime.datetime.now().date()
    from_date = to_date - datetime.timedelta(days = delta)

    data = kite.historical_data(instrument_token=token,from_date=from_date,to_date=to_date,interval=interval)
    df = pd.DataFrame(data)
    return df

#def telegram_bot_message(bot_message):
 #   bot_token = '5176697427:AAE-h4YW5_9emfubhYmQIN6chco0_214FLU',
  #  bot_chatID = '1283565668' 
   # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
    #'&parse_mode=MarkdownV2&text=' + bot_message
    #response = requests.get(send_text)
    #return response.json()

def finder(ltp, multiplier,name,expiry,ce_pe):
    step_value=step_values[name]
    atm_strike = round(ltp/step_value)*step_value + multiplier*step_value
    option_name = name + expiry+str(atm_strike) + ce_pe
    return option_name

def send_CE_to_file(CE):    
    file = open(ce_filename, 'w')
    file.write(CE)
    file.close()

def send_PE_to_file(PE):    
    file = open(pe_filename, 'w')
    file.write(PE)
    file.close()

def send_CEavg_to_file(avg_ce):    
    file = open(ce_avg, 'w')
    file.write(avg_ce)
    file.close()

def send_PEavg_to_file(avg_pe):    
    file = open(pe_avg, 'w')
    file.write(avg_pe)
    file.close()


def finder(ltp, multiplier,name,expiry,ce_pe):
    step_value=step_values[name]
    atm_strike = round(ltp/step_value)*step_value + multiplier*step_value
    option_name = name + expiry+str(atm_strike) + ce_pe
    return option_name


##############################################################################################################################################################
import neo_api_client
from neo_api_client import NeoAPI
import pdb

ck = "GdyW3K8GuCevSfhnCRlxL85EbU0a"
cs = "ITuS63wPnASfYogw83bk1m8r3gQa"
mob = "+916281816653"
pwd = "Unix!@123"
at = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQ0NDg5MyIsImF1dCI6IkFQUExJQ0FUSU9OIiwiYXVkIjoiR2R5VzNLOEd1Q2V2U2ZobkNSbHhMODVFYlUwYSIsIm5iZiI6MTcxMzcwMTc4MCwiYXpwIjoiR2R5VzNLOEd1Q2V2U2ZobkNSbHhMODVFYlUwYSIsInNjb3BlIjoiZGVmYXVsdCIsImlzcyI6Imh0dHBzOlwvXC9uYXBpLmtvdGFrc2VjdXJpdGllcy5jb206NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjozNjAwMTcxMzcwMTc4MCwiaWF0IjoxNzEzNzAxNzgwLCJqdGkiOiJhZTFlMjdjMi1mYzlmLTQwZTktYjY1My1kZmI4NDZlYjgxNTUifQ.HYoarNV4A7uuIf24ZwL2rPVg5sG9Dx-ro1O_uMnEG0P8gZrgS_pozcq-bx9xZn0nCD259b1rVuHWVYRyn1vHcIoYGHfcBbmoBszTE2uDZdhOxiFOngDmICl2mpdE1-8NTccisgMSEaXuz1EvY20SMT4UzmYraX6otHWcptYp4_o-uUfNoWF0Zl59ltTQs5NNeCej9PuPw4LUyVu7trN7m01AywbVBaxlKx3_PBCYHQypUcAX0g69ECFUgmdTMBD7kph9W69HjgPr6OOyjnLkaqYmOJ8rlL7g2eBlGUovCe_IptHrUCy3qGd3X7kYYNFF9gBOAMlBOemkQGE08FEICw"

client = NeoAPI(consumer_key=ck, consumer_secret=cs, environment='PROD', access_token=at, neo_fin_key=None)
client.login(mobilenumber=mob, password=pwd)
otp = 0
pdb.set_trace()
client.session_2fa(OTP=otp)


##################################################################################################################################################################


qty = 25
traded_limit = 0
traded_list = []
ce_traded = []
pe_traded = []
pe_price = []
ce_price = []
cost = []
ce_traded_status = 0
pe_traded_status = 0

# 1  === real
# 2 === paper

trade_type = 1
print(" hi have a good day and  i have logged")

nse = 5


if nse == 1:
    watchlist = ['NIFTY BANK']
    op = "BANKNIFTY"
    qty = 15*3
    PP = "NFO:"
    typex = "NSE:"
    kk = "nse_fo"   
    hh = "24APR" 

if nse == 2:
    watchlist = ['NIFTY 50']
    op = "NIFTY"
    qty = 50
    typex = "NSE:"
    kk = "nse_fo" 
    PP = "NFO:" 
    hh = "24APR"  
    #MONTLY 24APR, WEEKLY:YRMD

if nse == 3:
    watchlist = ['NIFTY FIN SERVICE']
    op = "FINNIFTY"
    qty = 40
    typex = "NSE:"
    kk = "nse_fo" 
    PP = "NFO:" 
    hh = "24APR"  

if nse == 4:
    watchlist = ['SENSEX']
    op = "SENSEX"
    qty = 10*2
    typex = "BSE:"
    kk = "bse_fo"  
    PP = "BFO:"
    hh = "24APR"  

if nse == 5:
    watchlist = ['BANKEX']
    op = "BANKEX"
    qty = 15*3
    typex = "BSE:"
    kk = "bse_fo"  
    PP = "BFO:"
    hh = "24APR"



for name in watchlist:
    ltp = kite.ltp([typex + name])[typex + name]['last_price']
    if ltp not in cost:
        cost.append(ltp)




#data calling
while True:    
    for name in watchlist:
        df = get_data(name , typex, 10, '5minute' , False)
        df = df.set_index(df['date'])

        ltp = str(cost)[1:-1]
        ltp = int(float(ltp))        

        CE = finder(ltp,-1, op,hh,'CE')
        PE = finder(ltp,1,op,hh,'PE')


        #DATA CALLING FOR CE_PE
        df_ce = get_data( CE, PP, 10, '5minute',False)
        df_pe = get_data( PE, PP, 10, '5minute',False)

        ce_ltp = kite.ltp([PP + CE])[PP + CE]['last_price']
        pe_ltp = kite.ltp([PP + PE])[PP + PE]['last_price']


        qty = str(qty)

        lc = df.iloc[-2]
        slc = df.iloc[-3]
        tlc = df.iloc[-4]

        ce_lc = df_ce.iloc[-2]
        pe_lc = df_pe.iloc[-2]

        

        ce_slc = df_ce.iloc[-3]
        pe_slc = df_pe.iloc[-3]
        


        buy_sl = slc['low']
        sell_sl = slc['high']




        avg_ce = kite.quote(PP + CE)[PP + CE]['average_price']
        avg_pe = kite.quote(PP + PE)[PP + PE]['average_price']


######################################################################################################################################################################
############################################################################################################################################################################

    if traded_limit == 0:
        print("Scanning  :-", CE,"  ", PE,"  ltp_ce  ",ce_ltp,"  avg_ce  ",avg_ce,"  ltp pe  ",pe_ltp,"  pe avg  ",avg_pe)





##############################################################################################################################################################
    if traded_limit == 1 and trade_type==1:
        file = open(ce_filename, 'r+')
        exit_ce = file.read()
        ce_ltp = kite.ltp([PP + exit_ce])[PP + exit_ce]['last_price']
        res = str(ce_price)[1:-1]
        res = int(float(res))
        ce_target = round(res + 120)
        ce_stoploss = round(res - 3)

        print("time for the target" + str(ce_target) +" and stoploss"+ str(ce_stoploss)+" in ce")


        if ce_ltp > ce_target:
            print("exited from posistions1")
            traded_limit = 0
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_ce,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)


        if ce_ltp < ce_stoploss:
            file = open(ce_filename, 'r+')
            exit_ce = file.read()
            traded_limit = 0
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_ce,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)
            print("exited from posistions2")


        if  (pe_ltp < avg_pe+1)  and (PE not in pe_traded) and (pe_traded_status == 0) and (traded_limit == 0)  and (trade_type == 1):
            pe_traded_status = 1
            sd = (pe_ltp > avg_pe+1)
            print("one cond done too and   ", sd)
    
        if (pe_ltp > avg_pe+1) and pe_traded_status == 1 and traded_limit == 0:
            pe_traded.append(PE)
            send_PE_to_file(PE)
            traded_status = 1
            traded_limit = 3
            print(f"buy   :-", PE)
            pe_price.append(pe_ltp)
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=PE,transaction_type='B', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)


##############################################################################################################################################################################
#######################################################################################################################################################################################

    if traded_limit == 2 and trade_type==1:
        file = open(pe_filename, 'r+')
        exit_pe = file.read()
        pe_ltp = kite.ltp([PP + exit_pe])[PP + exit_pe]['last_price']
        res = str(pe_price)[1:-1]
        res = int(float(res))
        pe_target = round(res + 40)
        pe_stoploss = round(res - 3)
    

        print("time for the target" + str(pe_target)+ " and stoploss"+ str(pe_stoploss)+" in pe")


        if pe_ltp > pe_target:
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_pe,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)
            
            traded_limit = 0
            print("exited from posistions3")
            pe_traded.pop()
            pe_price.pop()
            pe_traded_status = 0

        if pe_ltp < pe_stoploss:
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_pe,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)
            traded_limit = 0
            pe_traded_status = 0
            print("exited from posistions4")
            pe_traded.pop()
            pe_price.pop()
    
        if  (ce_ltp < avg_ce) and (CE not in ce_traded) and (ce_traded_status == 0) and (traded_limit == 0) and (trade_type == 1):
    
            ce_traded_status = 1
            ss = (ce_ltp > avg_ce+1)
            print("one cond done  and  ",ss,ce_traded_status)
    
        if (ce_ltp > avg_ce+1) and ce_traded_status == 1 and traded_limit == 0:
            traded_limit = 3
            ce_traded.append(CE)
            ce_price.append(ce_ltp)        
            traded_status = "yes"
            send_CE_to_file(CE)
            print(f"buy   :- ", CE)

            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=CE,transaction_type='B', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)

    


################################################################################################################################################################################################
    if traded_limit == 3 and trade_type==1:

        ce_file = open(ce_filename, 'r+')
        exit_ce = ce_file.read()
        ce_ltp = kite.ltp([PP + exit_ce])[PP + exit_ce]['last_price']

        pe_file = open(ce_filename, 'r+')
        exit_pe = pe_file.read()
        pe_ltp = kite.ltp([PP + exit_pe])[PP + exit_pe]['last_price']
    

        res = str(pe_price)[1:-1]
        res = int(float(res))

        ress = str(ce_price)[1:-1]
        ress = int(float(ress))

        pe_target = round(res + 40)
        pe_stoploss = round(res - 3) 

        ce_target = round(ress + 120)
        ce_stoploss = round(ress - 3)        

        print("time for the target" + str(ce_target) +" and stoploss"+ str(ce_stoploss)+" in ce")

        if ce_ltp > ce_target:
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_ce,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)

            print("exited from posistions1")
            traded_limit = 2
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0


        if ce_ltp < ce_stoploss:
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_ce,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)

            traded_limit = 2
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0
           
            print("exited from posistions2")

        if pe_ltp > pe_target:
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_pe,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)
            print("exited from posistions1")
            traded_limit = 1
            pe_traded.pop()
            pe_price.pop()
            pe_traded_status = 0

        if pe_ltp < pe_stoploss:
            traded_limit = 1
            client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=exit_pe,transaction_type='S', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)

            print("exited from posistions2")
            pe_traded.pop()
            pe_price.pop()
            pe_traded_status = 0

########################################################################################################################################################################################################################################################################################
##############################################################################################################################################################
    if traded_limit == 1 and trade_type == 2:
        file = open(ce_filename, 'r+')
        exit_ce = file.read()
        ce_ltp = kite.ltp([PP + exit_ce])[PP + exit_ce]['last_price']
        res = str(ce_price)[1:-1]
        res = int(float(res))
        ce_target = round(res + 120)
        ce_stoploss = round(res - 3)

        print("time for the target" + str(ce_target) +" and stoploss"+ str(ce_stoploss)+" in ce")


        if ce_ltp > ce_target:
            print("exited from posistions1")
            traded_limit = 0
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0
           
            

        if ce_ltp < ce_stoploss:
            file = open(ce_filename, 'r+')
            exit_ce = file.read()
            traded_limit = 0
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0
           
            
            print("exited from posistions2")

        if  (pe_ltp < avg_pe+1)  and (PE not in pe_traded) and (pe_traded_status == 0) and (traded_limit == 0)  and (trade_type == 1):
            pe_traded_status = 1
            sd = (pe_ltp > avg_pe+1)
            print("one cond done too and   ", sd)
    
        if (pe_ltp > avg_pe+1) and pe_traded_status == 1 and traded_limit == 0:
            pe_traded.append(PE)
            send_PE_to_file(PE)
            traded_status = 1
            traded_limit = 3
            print(f"buy   :-", PE)
            pe_price.append(pe_ltp)

###########################################################################################################################################################################
#######################################################################################################################################################################################

    if traded_limit == 2 and trade_type == 2:
        file = open(pe_filename, 'r+')
        exit_pe = file.read()
        pe_ltp = kite.ltp([PP + exit_pe])[PP + exit_pe]['last_price']
        res = str(pe_price)[1:-1]
        res = int(float(res))
        pe_target = round(res + 40)
        pe_stoploss = round(res - 3)
    

        print("time for the target" + str(pe_target)+ " and stoploss"+ str(pe_stoploss)+" in pe")

        if pe_ltp > pe_target:   
            traded_limit = 0
            print("exited from posistions3")
            pe_traded.pop()
            pe_price.pop()
            pe_traded_status = 0

        if pe_ltp < pe_stoploss:
            traded_limit = 0
            print("exited from posistions4")
            pe_traded.pop()
            pe_price.pop()
            pe_traded_status = 0

        if  (ce_ltp < avg_ce) and (CE not in ce_traded) and (ce_traded_status == 0) and (traded_limit == 0) and (trade_type == 1):
            ce_traded_status = 1
            ss = (ce_ltp > avg_ce+1)
            print("one cond done  and  ",ss,ce_traded_status)
    
        if (ce_ltp > avg_ce+1) and ce_traded_status == 1 and traded_limit == 0:
            traded_limit = 3
            ce_traded.append(CE)
            ce_price.append(ce_ltp)        
            traded_status = "yes"
            send_CE_to_file(CE)
            print(f"buy   :- ", CE)




################################################################################################################################################################################################
    if( traded_limit == 3) and (trade_type == 2):

        ce_file = open(ce_filename, 'r+')
        exit_ce = ce_file.read()
        ce_ltp = kite.ltp([PP + exit_ce])[PP + exit_ce]['last_price']

        pe_file = open(ce_filename, 'r+')
        exit_pe = pe_file.read()
        pe_ltp = kite.ltp([PP + exit_pe])[PP + exit_pe]['last_price']
    

        res = str(pe_price)[1:-1]
        res = int(float(res))

        ress = str(ce_price)[1:-1]
        ress = int(float(ress))

        pe_target = round(res + 40)
        pe_stoploss = round(res - 3)

        ce_target = round(ress + 120)
        ce_stoploss = round(ress - 3)        

        print("time for the target" + str(ce_target) +" and stoploss"+ str(ce_stoploss)+" in ce")

        if ce_ltp > ce_target:
           
            print("exited from posistions1")
            traded_limit = 2
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0


        if ce_ltp < ce_stoploss:
            traded_limit = 2
            ce_traded.pop()
            ce_price.pop()
            ce_traded_status = 0
           
            print("exited from posistions2")

        if pe_ltp > pe_target:
           

            print("exited from posistions1")
            traded_limit = 1
            pe_traded.pop()
            pe_price.pop()
            pe_traded_status = 0

        if pe_ltp < pe_stoploss:
            file = open(ce_filename, 'r+')
            exit_ce = file.read()
            traded_limit = 1
            pe_traded_status = 0

            print("exited from posistions2")
            pe_traded.pop()
            pe_price.pop()


##########################################################################################################################################################################################################################################################################################

    if  (ce_ltp < avg_ce) and (CE not in ce_traded) and (ce_traded_status == 0) and (traded_limit == 0) and (trade_type == 2):
        if (ce_ltp > avg_ce+1):
            traded_limit = 1
            ce_traded.append(CE)
            ce_price.append(ce_ltp)        
            traded_status = "yes"
            send_CE_to_file(CE)
            print(f"buy   :- ", CE)

    if  (pe_ltp > avg_pe+1)  and (PE not in pe_traded) and (pe_traded_status == 0) and (traded_limit == 0)  and (trade_type == 2):
        if (pe_ltp < avg_pe+1):
            pe_traded.append(PE)
            send_PE_to_file(PE)
            traded_status = "yes"
            traded_limit = 2
            print(f"buy   :-", PE)
            pe_price.append(pe_ltp)

##########################################################################################################################################################################################
###################################################################################################################################################################################################
    if  (ce_ltp < avg_ce) and (CE not in ce_traded) and (ce_traded_status == 0) and (traded_limit == 0) and (trade_type == 1):

        ce_traded_status = 1
        ss = (ce_ltp > avg_ce+1)
        print("one cond done  and  ",ss,ce_traded_status)

    if (ce_ltp > avg_ce+1) and ce_traded_status == 1 and traded_limit == 0:
        traded_limit = 1
        ce_traded.append(CE)
        ce_price.append(ce_ltp)        
        traded_status = "yes"
        send_CE_to_file(CE)
        print(f"buy   :- ", CE)
        key = client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=CE,transaction_type='B', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)
        print(key)


    if  (pe_ltp < avg_pe+1)  and (PE not in pe_traded) and (pe_traded_status == 0) and (traded_limit == 0)  and (trade_type == 1):
        pe_traded_status = 1
        sd = (pe_ltp > avg_pe+1)
        print("one cond done too and   ", sd)

    if (pe_ltp > avg_pe+1) and pe_traded_status == 1 and traded_limit == 0:
        pe_traded.append(PE)
        send_PE_to_file(PE)
        traded_status = 1
        traded_limit = 2
        print(f"buy   :-", PE)
        pe_price.append(pe_ltp)
        key = client.place_order(exchange_segment=kk, product='NRML', price='0', order_type='MKT', quantity=qty, validity='DAY', trading_symbol=PE,transaction_type='B', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)
        print(key)




 ###########################################################################################################################################################################################################################################################        
