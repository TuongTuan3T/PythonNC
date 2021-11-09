from flask import Flask
ungdung = Flask(__name__)
@ungdung.route('/')
def hello():
    tentruong='Dai hoc Van Lang!'
    lienket= '<a href="https://www.vanlanguni.edu.vn">' +tentruong+'</a><br>'
    chuoi = lienket
    import datetime
    nam =datetime.date.today().year
    chuoi = chuoi+'<b>Xin<i> chao</i> Tan sinh vien nam' + str(nam) +'!</b>'
    return chuoi

@ungdung.route('/monhoc')
def learn():
    chuoi='đây là trang môn học!'
    return chuoi

@ungdung.route('/monhoc/<tenmon>')  
def subjects(tenmon):
    chuoi = 'Đây là trang môn học'
    monhoc=str(tenmon).upper()
    if monhoc=="":
        chuoi = chuoi + "!"
    else:
        chuoi =chuoi + ""+monhoc
    return chuoi

@ungdung.route('/sinhvien/')
def strudents():
    chuoi ='Đây là trang các khóa học!'
    return chuoi

@ungdung.route('/sinhvien/<int:namhoc>')
def school_year(namhoc):
    chuoi = 'đây là năm học'
    nam= str(namhoc).upper()
    if nam== "":
        chuoi = chuoi+"!"
    else:
        chuoi =chuoi+ " "+ nam
    return chuoi

if __name__ =="__main__":
    ungdung.run(port=5050)
