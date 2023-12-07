local time = {44, 70, 70, 80}
local dist = {283, 1134, 1134, 1491}
local ways = {0, 0, 0, 0}

-- spoiler start ||
for i = 1, 4 do
    for t = 1, time[i] do
        if t * (time[i] - t) >= dist[i] then ways[i] = ways[i] + 1 end
    end
end

local time_p2 = 44707080
local dist_p2 = 283113411341491
local ans = 0
for t = 1, time_p2 do
    if t * (time_p2 - t) >= dist_p2 then ans = ans + 1 end
end

client:getChannel("1144290626255462444"):send(ways[1] * ways[2] * ways[3] * ways[4])
client:getChannel("1144290626255462444"):send(ans)
-- || spoiler end