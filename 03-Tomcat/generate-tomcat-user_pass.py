#!/usr/bin/python3

with open("user.txt", "r") as fu:
    with open("pass.txt", "r") as fp:
        with open("user-pass.txt", "w") as fn:
            fuser = fu.readlines();
            fpass = fp.readlines();
            for i in fuser:
                for j in fpass:
                    new = i.strip("\n") + ":" + j.strip("\n");
                    print(new);
                    fn.write(new + "\n");
