from django.db import models
import enum

# Create your models here.
class Zone(enum.Enum):
    Mango:1
    Kadma:2
    Sonari:3
    Bistupur:4
    Sakchi:5
    Golmuri:6
    Jugsalai:7
    Burmamines:8
    Telco:9
    Parsudh:10

class ItemCategory(enum.Enum):
    Groceries:"GRO"
    Dairy:"DAI"
    Vegetables:"VEG"
    Medicine:"MED"
    Baby:"BAB"

class Shop(models.Model):
    shopId=models.AutoField(primary_key=True);
    shopName=models.CharField(max_length=50);
    shopZone=models.IntegerField(choices=Zone);
    shopContact=models.CharField(max_length=10);
    itemList = [];

    def __str__(self):
        return self.shopName;

    def __init__(self,shopName,shopZone,shopContact,itemList):
        self.shopName=shopName;
        self.shopZone=shopZone;
        self.shopContact=shopContact;
        self.itemList=itemList;

class User(models.Model):
    userId=models.AutoField(primary_key=True);
    userName=models.CharField(max_length=50);
    userAddress=models.CharField(max_length=100);
    userContact=models.CharField(max_length=10);
    def __str__(self):
        return self.userName;

    def __init__(self,userName,userAddress,userContact):
        self.userName=userName;
        self.userAddress=userAddress;
        self.userContact=userContact;

class Item(models.Model):
    itemId=models.AutoField(primary_key=True);
    itemName=models.CharField(max_length=50);
    itemPrice=models.IntegerField();
    itemqty=models.IntegerField();
    itemqtyAdd=models.IntegerField();
    itemType=models.CharField(max_length=3,choices=ItemCategory)
    def __str__(self):
        return self.itemName;

    def __init__(self,itemName,itemPrice,itemqty,itemType):
        self.itemName=itemName;
        self.itemPrice=itemPrice;
        self.itemqty=itemqty;
        self.itemType=itemType;
        self.itemqtyAdd=0;


class Request(models.Model):
    requestId=models.AutoField(primary_key=True);
    itemsList = [];
    totalAmount = models.IntegerField();

    def __init__(self,itemsList,totalAmount):
        self.itemsList=itemsList;
        self.totalAmount=totalAmount;

class FinalBill(models.Model):
    requestId=models.IntegerField();
    itemsList = [];
    totalAmount = models.IntegerField();

    def __init__(self,requestId,itemsList,totalAmount):
        self.requestId=requestId;
        self.itemsList=itemsList;
        self.totalAmount=totalAmount;
