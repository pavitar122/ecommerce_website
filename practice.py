  if password != confirm_password:
            messages.warning(request,"Password Not Matching")
            return redirect("/auth/signup")
        
        if User.objects.filter(email = email).first():
            messages.warning(request,"Email already exists")
            return redirect("/auth/signup")
        
        if User.objects.filter(username = username).first():
            messages.warning(request,"Username already exists")
            return redirect("/auth/signup")
        
        user_obj = User.objects.create(username= username , email=email)
        user_obj.set_password(password)
        user_obj.save()

        auth_token = str(uuid.uuid4())
        profile_obj = Profile.objects.create(user=user_obj, auth_token = auth_token )
        send_mail_to_user(email=email ,token= auth_token )
        profile_obj.save()

        messages.success(request,"Email sent to you.")
        return render(request, "signup.html")