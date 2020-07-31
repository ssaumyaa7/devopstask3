import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("saumya4799@gmail.com", "9687778393")
message = "Error in site... Check code, push to start again"
s.sendmail("saumya4799@gmail.com", message)
s.quit()
