import mysql.connector as sq
conn=sq.connect(host="localhost" ,user="root" , passwd="pk123" ,database="fbs")
mycursor = conn.cursor()
mycursor.execute("CREATE TABLE MRECORD(SNO INTEGER(4) AUTO_INCREMENT, Receipt varchar(15), bdate date, Sprite INTEGER(6), Pepsi INTEGER(6) , DietCoke INTEGER(6) , Mojito INTEGER(6) ,\
                  Cappuccino INTEGER(6) , Fanta INTEGER(6) , CocaCola INTEGER(6) , coldcoffee INTEGER(6), HogDog INTEGER(6) , VegBurger INTEGER(6) \
                , Pasta INTEGER(6), Rice_Plate INTEGER(6), Sandwich INTEGER(6) , Fires INTEGER(6) , Spagetti INTEGER(6) , Fazitas INTEGER(6) ,\
                  COST_OF_DRINKS FLOAT(11,2), TAXPAID FLOAT(11,2) , COST_OF_FOODS FLOAT(11,2) , SUBTOTAL FLOAT(11,2) , SERVICE_CHARGE FLOAT(11,2) , TOTALCOST FLOAT(11,2), PRIMARY KEY(SNO));")
#mycursor.execute("DROP TABLE MRECORDS;")
conn.commit()
conn.close

''' Receipt_Ref.get(), DateofOrder.get() ,E_Sprite.get(), E_Pepsi.get(), E_DietCoke.get(), E_Mojito.get(), E_Cappuccino.get(), E_Fanta.get(), E_CocaCola.get(), E_ColdCoffee.get(), \
          E_HotDog.get(),  E_VegBurger.get(), E_Pasta.get(), E_HamBurger.get(), E_Sandwich.get(), E_Fires.get(), E_Spagetti.get(), E_Fazitas.get(), \
          CostofDrinks.get(), PaidTax.get(), CostofFood.get(), SubTotal.get(), ServiceCharge.get(), TotalCost.get() '''
