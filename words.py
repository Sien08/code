target = 4500
done = int(input("你已经背了多少个词？"))
per_day = int(input("你每天打算背多少个？"))
left = target - done
days = left / per_day
print(f"还差 {left} 个词，大约需要 {days:.0f} 天")
print(f"大约 {days/7:.0f} 周")