import datetime

class invoice():
  # Generates the HTML invoice for every successful charge
  def __init__(self):
    pass

  def gen_ros(self, fileName, userID, email, fName, lName, address, city, state, zipcode, price):
    brand = "brandName"
    now = datetime.datetime.now()
    file = open("data/receipts/html/" + fileName + now.strftime("%Y-%m-%d") + ".html", "w") 
    file.write('<!DOCTYPE html><html lang="en"><head><title>${brand} Invoice</title><meta charset="utf-8"><meta name="theme-color" content="#000000"><meta name="viewport" content="width=540, user-scalable=1"><link rel="stylesheet" type="text/css" href="../style/invoice.css" /><link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Oswald" /><link href="https://fonts.googleapis.com/css?family=Titillium+Web&display=swap" rel="stylesheet"><link href=\'https://fonts.googleapis.com/css?family=Spectral\' rel=\'stylesheet\' /></head><body class="enter pge-enter"><main class="invoice">  <div class="top">    <div class="biz-info">      <div class="brand">${brand}</div>      <div class="title">RECORD OF SALE</div>    </div>    <div class="cust-info">')
    file.write('<div class="cust-name">' + fName + ' ' + lName+ '</div>') 
    file.write('<div class="full-address"><div class="cust-address">' + address + '</div><div class="city">' + city +'</div><div class="state">' + state + '</div><div class="zipcode">' + zipcode + '</div></div>')
    file.write('</div></div><div class="middle">  <div class="heading">    <div class="desc">      <div class="title">CUSTOMER SUMMARY</div>      <div class="text"></div>    </div>  </div>  <div class="cust-info">')
    file.write('<div class="name"><div class="title">CUSTOMER NAME</div><div class="cust-name">' + fName + ' ' + lName + '</div></div>')
    file.write('<div class="id"><div class="title">CUSTOMER ID</div><div class="cust-name">' + userID + '</div></div>')
    file.write('<div class="address"><div class="title">BILLING ADDRESS</div><div class="info"><div class="cust-address">' + address + '</div><div class="city">' + city + '</div><div class="state">' + state + '</div><div class="zipcode">' + zipcode + '</div></div></div>')
    file.write('<div class="email"><div class="title">EMAIL</div><div class="cust-email">' + email + '</div></div>')
    file.write('<div class="INVOICE DATE"><div class="title">DATE</div><div class="cust-date">' + now.strftime("%Y-%m-%d %H:%M:%S") + '</div></div>')
    file.write('<div class="PLATFORM"><div class="title">PLATFORM</div><div class="cust-date">SQUARE</div><div class="cust-date">Notes:  Subscription Charge</div></div>')
    file.write('</div></div><div class="bottom"><div class="heading"><div class="desc"><div class="title">SALE DESCRIPTION</div><div class="text"></div></div></div><div class="table"><div class="row upp"><div class="col">USER ID</div><div class="col">PARTNER ID</div><div class="col">SALE TYPE</div><div class="col">ACC LVL</div><div class="col">ACC PRICE</div><div class="col">ACC DSCT</div><div class="col">TAX (10%)</div><div class="col">TIP</div><div class="col">SALE DESC</div><div class="col">TOTAL PRICE</div><div class="col">PARTNER PROF</div><div class="col"> PROF</div><div class="col">PAYMENT STAT</div><div class="col">PARTNER STAT</div></div><div class="row">')
    file.write('<div class="col">' + userID +'</div><div class="col">N/A</div><div class="col">2</div><div class="col">N/A</div><div class="col">N/A</div><div class="col">N/A</div><div class="col">N/A</div><div class="col">N/A</div><div class="col"> Subscription Charge</div><div class="col">' + price +'</div><div class="col">0.00</div><div class="col">' + price + '</div><div class="col">' + 'SUCCESS' + '</div><div class="col">N/A</div>')
    file.write('</div></div><div class="final"><div class="subtotal"><div class="total-price price-dollar"><div class="total">Subtotal (Tax Included):</div><div class="total-dollar">$ ' + price + '</div></div><div class="total-due price-dollar"><div class="total">Due Today:</div><div class="total-dollar">$ ' + price + '</div></div></div><div class="copyright"><div class="biz"><div class="div1">${brand}</div><div class="div2">Copyright© 2021 | domain LLC | Jacksonville, FL</div></div><div class="contact"><br/>${brand}.com | support@${brand}.com</div></div></div></div></main><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script><script>window.jQuery || document.write(\'<script type="text/javascript" src="../../JAVASCRIPT/PLUGINS/JQUERY/jquery-3.x.x.min.js"><\/script>\')</script></body></html>')
    file.close() 