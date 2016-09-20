import glob
import ExtractMsg

for filename in glob.iglob('*.msg'):
    try:
        ExtractMsg.Message(filename).simple_save()
    except:
        print 'Read of ', filename, ' failed!'

print 'All done!'
