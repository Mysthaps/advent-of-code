local _, inp = http.request("GET", 'https://cdn.discordapp.com/attachments/861929980757016606/1181608375746838558/message.txt')

-- spoiler start ||
local function split(inpstr, sep)
    local t = {}
    for str in string.gmatch(inpstr, "([^"..sep.."]+)") do
        table.insert(t, str)
    end
    return t
end

local inplines = split(inp, "//")
local seeds = split(inplines[1], " ")
for x, v in pairs(seeds) do
    seeds[x] = tonumber(v)
end

for i = 2, 8 do
    local rules = split(inplines[i], "\n")
    for x, v in pairs(seeds) do
        local done = false
        for idx, rule in pairs(rules) do
            local t_rule = split(rule, " ")
            for rx, rv in pairs(t_rule) do
                t_rule[rx] = tonumber(rv)
            end
            if t_rule[1] ~= nil then
                if v >= t_rule[2] and v <= t_rule[2] + t_rule[3] - 1 and done == false then
                    seeds[x] = t_rule[1] + seeds[x] - t_rule[2]
                    done = true
                end
            end
        end
    end
    print()
end

table.sort(seeds)
client:getChannel("1144290626255462444"):send(seeds[1])
-- || spoiler end