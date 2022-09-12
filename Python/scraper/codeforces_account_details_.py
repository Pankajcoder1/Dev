from bs4 import BeautifulSoup
import requests


def codeforces_account_details(link):
	
	current_rank=""
	user_id=""
	current_rating=""
	highest_rank=""
	highest_rating=""
	total_contest=""
	contest_page_url=""
	contest_page_link=""
	country=""
	email=""
	current_status=""

	try:
		page_url=requests.get(link)
		if(page_url.status_code!=200):
			print(f"Account access request failed ....:{page_url.status_code}")
		else:
			soup=BeautifulSoup(page_url.content,"html.parser")

			# rank get here.
			current_rank=soup.find("div",class_="user-rank").find("span")
			current_rank=str(current_rank.contents[0])

			# user-id
			if(current_rank[0]=='L'):
				user_id=soup.find("h1").find("a",class_="rated-user")
				# if user are Legendary Grandmaster then i first scrap the first letter
				# (which is store in user_id_f) of his name and then rest in user_id
				user_id_f=str(user_id.contents[0].contents[0])
				user_id=user_id_f+str(user_id.contents[1])
			else:
				user_id=soup.find("h1").find("a",class_="rated-user")
				user_id=str(user_id.contents[0])

			# highest rank
			highest_rank=soup.find("span",class_="smaller").find("span")
			highest_rank=str(highest_rank.contents[0])
			highest_rank=highest_rank.split(',')[0]

			# highest rating
			highest_rating=soup.find("span",class_="smaller").findChildren()[1].contents[0]
			highest_rating=int(highest_rating)

			#current rating
			current_rating=soup.find("div",class_="info").find("ul").findChildren()[2].contents
			current_rating=int(current_rating[0])

			# country
			try:
				if(user_id[0]=='L'):
					country=soup.find("div",class_="main-info").findChildren()[8].contents[0]
					country=str(country)
				else:
					country=soup.find("div",class_="main-info").findChildren()[7].contents[0]
					country=str(country)
			except:
				country=None
				print("country name not provided yet.")

			#email
			try:
				email=soup.find("div",class_="info").find("ul").findChildren()[11].contents[2]
				email=str(email).split('\n')[3].split(' ')[24]
				email=str(email)
			
			except:
				email=None
				print("email is not provided")

			# current_status
			# here if email is not provided the due to one 
			# less li tag code is changed
			if(email!=None):
				current_status=soup.find("div",class_="info").find("ul").findChildren()[13].find("span").contents[0]
				current_status=str(current_status)
			else:
				current_status=soup.find("div",class_="info").find("ul").findChildren()[12].contents[0]
				current_status=str(current_status)

			# contest number
			contest_page_link="https://codeforces.com/contests/with/"+user_id
			contest_page_url=requests.get(contest_page_link)
			if(contest_page_url.status_code!=200):
				print(f"Account access request failed ....:{page_url.status_code}")
			else:
				soup2=BeautifulSoup(contest_page_url.content,"html.parser")
				total_contest=soup2.find("table",class_="user-contests-table").find("tbody").find("tr").find("td").contents[0]
				total_contest=int(total_contest)

			# now display all details on screens
			print("\tAll extracted details here ... ")
			print("user id is ",user_id)
			if(email!=None):
				print(f"Email of {user_id} is ",email)
			print("current rank is ",current_rank)
			print("current rating is ",current_rating)
			print("highest rank is ",highest_rank)
			print("highest rating is ",highest_rating)
			print(f"total rated contest by {user_id} is {total_contest}")
			if(current_status=="online now"):
				print(f"user {user_id} is online now")
			else:
				print(f"last visit of {user_id} is  ",current_status)
			if(country!=None):
				print("country is ",country)
			
	except:
		print("Invalid user url entered ...")
	

print("Enter link first : ",end=" ")
link=input()

codeforces_account_details(link)