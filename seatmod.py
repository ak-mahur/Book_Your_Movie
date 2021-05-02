from usermod import user
class seat:
    user_list={}
    def __init__(self,Tr,Tc,r,c):
        self.Availability=True
        self.Price=self.price_calculator(Tr,Tc,r,c)

    def bookseat(self,rno,cno):
        seat.user_list[(rno*100)+cno]=user()         #multiplying rno(row number) by 100 so that unique keys can be formed for more than 10 columns
        seat.user_list[(rno * 100) + cno].set_user_info()
        self.Availability=False

    def price_calculator(self,tr,tc,sr,sc):
        if tr*tc <=60:
            return 10
        elif sr<= tr//2:
            return 10
        else:
            return 8









