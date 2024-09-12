if __name__ == '__main__':
    print("Please input three numbers")
    t = 1
    nums = []
    while t <= 3:
        user_input = input(f"User input {t}: ")
        if not user_input:
            continue
        nums.append(int(user_input))
        t += 1
    nums.sort()
    can_form = nums[0] + nums[1] > nums[2]
    print(
        ("Yes" if can_form else "No") +
        ", these three lengths " +
        ("can" if can_form else "cannot") +
        " form a triangle."
    )
    