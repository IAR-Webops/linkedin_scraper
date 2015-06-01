require 'mechanize'

agent = Mechanize.new

USERNAME = 'dharani.manne@gmail.com'
PASSWORD = 'amulyaabhi'

main_page = 'https://www.linkedin.com/edu/alumni?id=13501'

home_page = agent.get('http://www.linkedin.com')
sign_in_link = home_page.links.find{|link| link.text == "Sign In"}
login_form = sign_in_link.click.form('login')
login_form.set_fields(:session_key => USERNAME, :session_password => PASSWORD)
return_page = agent.submit(login_form, login_form.buttons.first)
