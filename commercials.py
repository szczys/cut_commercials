#!/usr/bin/env python3
import datetime

string="ffmpeg -ss %s -i %s -t %s -c:v libx264 -c:a aac %s"
infile='video_with_commercials.ts'

segments = [
    ["00:00:09","00:03:52"],
    ["00:05:34","00:11:59"],
    ["00:14:10","00:26:08"],
    ["00:29:44","00:41:17"],
    ["00:45:25","00:56:43"],
    ["00:58:15","01:00:59"]
]

def get_diff(s,e):
    st = datetime.datetime.strptime(s, "%H:%M:%S")
    et = datetime.datetime.strptime(e, "%H:%M:%S")
    diff = et-st
    return(diff)

segmentnames = []
commands = []
for i,s in enumerate(segments):
    seg_name = "segment"+str(i)+".ts"
    duration = get_diff(*s)
    commands.append(string % (s[0],infile,duration,seg_name))
    segmentnames.append("file '%s'" % seg_name)

with open('inputs.txt', 'w') as f:
    f.writelines("\n".join(segmentnames))
    f.close()

commands.append("ffmpeg -f concat -i inputs.txt -c copy output.mp4")
print(" && \\".join(commands))
