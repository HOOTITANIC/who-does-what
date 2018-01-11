 password_list = ['*#*#','12345']
2.
3. def account_login():
4. tries = 3
5. while tries > 0:
6. password = input('Password:')
7. password_correct = password == password_list[-1]
8. password_reset = password == password_list[0]
9.
10. if password_correct:
11. print('Login success!')
12.
13. elif password_reset:
14. new_password = input('Enter Dnew password :')
15. password_list.append(new_password)
16. print('Password has changed successfully!')
17. account_login()
18. else:
19. print('Wrong password or invalid input!')
20. tries = tries - 1
21. print( tries, 'times left')
22.
23. else:
24. print('Your account has been suspended')
25.
26.account_login()
