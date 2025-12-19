import re
def check_password_strength(password):
 score=0
 suggestion=[]
 #Length check
 if len(password)>=12:
    score=score+1
 else:
    suggestion.append("Use atleast 12 characters ")
 #Uppercase Letters
 if re.search(r"[A-Z]", password):
    score=score+1
 else:
    suggestion.append("Add at least one uppercase letter. ")
 #lowercase letter
 if re.search(r"[a-z]", password):
    score=score+1
 else:
    suggestion.append("Add at least one lowercase letter. ")
 #Number Check
 if re.search(r"[0-9]", password):
    score=score+1
 else:
    suggestion.append("Add at least one number. ")
 #Special Characters
 if re.search(r"[!@#$%^&*().,?{}\\<>:]", password):
    score=score+1
 else:
    suggestion.append("Add at least one special character. ")
 return score, suggestion
def main():
 print("PASSWORD STRENGTH CHECKER")
 password=input("Enter your password: ")
 score, suggestion=check_password_strength(password)
 print("Password REPORT")
 print(f"Score: {score}/5")
 if score==5:
    print("Strong Password!")
 else:
    print("Weak Password! . Suggestion:")
 for i in suggestion:
    print(i)
if __name__ == "__main__":
    main()