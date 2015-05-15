from __future__ import ( division, absolute_import, print_function, unicode_literals )
from Tkinter import Label,Tk,Button,Entry
import sys, os, tempfile, logging
import pafy
if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse
#from download import filename
#url = "https://www.youtube.com/watch?v=LxQq8HTtb4A"
def download1(url):    
    video = pafy.new(url)
    print (video.title)
    print (video.rating)
    streams = video.streams
    i=0
    p=''
    for s in streams:
        print(s.resolution,i)
        print(s.url)
        p=p+s.resolution+'   '+str(i)+'\n'
        i=i+1
    Label( root, text=" {}".format(p)).grid(row=5,column=0)
    Label(root,text="select resolution").grid(row=4,column=0)
    
    #j=input()



def download(url,filename,resol, desc=None):
    video = pafy.new(url)
    print (video.title)
    print (video.rating)
    streams = video.streams
    l=len(streams)-1
    u = urllib2.urlopen(streams[int(resol)].url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(streams[int(resol)].url)
    #filename = "d:/{}.mp4".format("video")
    with open(filename, 'wb') as f:
        meta = u.info()
        meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])
        print("Downloading: {0} Bytes: {1}".format(url, file_size))
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = "{0:16}".format(file_size_dl)
            if file_size:
                status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
            status += chr(13)
            Label( root, text="Done:{0} size: {1}kb".format(file_size_dl * 100 / file_size, file_size/1024)).grid(row=6,column=0)
            #root.mainloop()
            print(status, end="")
        print()
    #return filename
#url =streams[j].url
#url="http://109.121.134.14/files/movies/13/62456/person.of.interest.422.hdtv-lol.mp4?ses=rMH22YzMhPKr5iHEoMVQYA&t=1431637157"
#filename = download_file(url)
#print(filename)
def close_window(): 
    root.destroy() 
if __name__ == '__main__':
    root = Tk()
    #font1 = tkFont.Font (family="Helvetica",size=12,weight="bold") 
    root.title("Downloader")
    label1 = Label( root, text='URL',bg="blue").grid(row=0,column=0)
    label2= Label( root, text='Download path').grid(row=1,column=0)
    e1= Entry(root)
    e1.grid(row=0,column=1)
    e2= Entry(root)
    e2.grid(row=1,column=1)
    e3 = Entry(root)
    e3.grid(row=4,column=1)
    Button(root,command=lambda:download(e1.get(),e2.get(),e3.get()) ,text='Download' ).grid(row=2,column=0)
    Button(root,text='Exit' ,command=lambda:close_window() ).grid(row=2,column=1)
    Button(root,text='Check' ,command=lambda:download1(e1.get())).grid(row=3,column=0)
    #Button(root,text='Instructions' ,command=lambda:readme()).grid(row=4,column=0)
    root.mainloop()