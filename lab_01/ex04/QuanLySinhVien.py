from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateId(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    def soLuongSinhVien(self):
        return len(self.listSinhVien)
    
    def nhapSinhVien(self):
        svID = self.generateId()
        name = input("Nhập tên sinh viên: ")
        sex = input("nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        DiemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svID, name, sex, major, DiemTB)
        self.XepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.getSinhVienByID(ID)
        if sv is not None:
            name = input("Nhập tên sinh viên: ")
            sex = input("nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành sinh viên: ")
            DiemTB = float(input("Nhập điểm trung bình sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._DiemTB = DiemTB
            self.XepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên với ID:", ID)
        def sortById(self):
            self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        def sortByName(self):
            self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        def sortByDiemTB(self):
            self.listSinhVien.sort(key=lambda x: x._DiemTB, reverse=False)
        def fineByID(self, ID):
            searchResult = None
            if (self.soLuongSinhVien() > 0):
                for sv in self.listSinhVien:
                    if (sv._id == ID):
                        searchResult = sv
            return searchResult
        def fineByName(self, keyword):
            listSV = []
            if (self.soLuongSinhVien() > 0):
                for sv in self.listSinhVien:
                    if (keyword.lower() in sv._name.lower()):
                        listSV.append(sv)
            return listSV
        def deleteById(self, ID):
            isDeleted = False
            sv = self.fineByID(ID)
            if (sv is not None):
                self.listSinhVien.remove(sv)
                isDeleted = True
            return isDeleted
        def xepLoaiHocLuc(self, sv:SinhVien):
            if (sv._DiemTB >= 8.0):
                sv.HocLuc = "Giỏi"
            elif (sv._DiemTB >= 6.5):
                sv.HocLuc = "Khá"
            elif (sv._DiemTB >= 5.0):
                sv.HocLuc = "Trung bình"
            else:
                sv.HocLuc = "Yếu"

            def showSinhVien(self, listSV):
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex,
                                                                     sv._major, sv._DiemTB, sv.HocLuc))
                if (listSV.__len__() > 0):
                    for sv in listSV:
                        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name,
                                                                             sv._sex, sv._major, sv._DiemTB, sv.HocLuc))
                print("\n")
            def getListSinhVien(self):
                return self.listSinhVien
            
              
