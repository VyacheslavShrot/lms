def cleanup_social_account(backend, uid, user=None, *args, **kwargs):
    print(backend)
    print(uid)
    print(user)
    print(args)
    print(kwargs)
    # user.photo = kwargs["response"]["avatar"]
    # user.save()v

    return {"user": user}
