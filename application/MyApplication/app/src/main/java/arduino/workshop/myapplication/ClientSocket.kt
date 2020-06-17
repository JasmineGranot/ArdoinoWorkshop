package arduino.workshop.myapplication

import android.os.AsyncTask
import java.io.*
import java.net.Socket

object ClientSocket : AsyncTask<String, Void, String>() {
    @ExperimentalStdlibApi
    public override fun doInBackground(vararg params: String?): String? {
        //val s = Socket("10.0.2.2", 65432)
        val s = Socket("192.168.1.13", 65432)
        //val s = MySocket.getSocket()
        val output = PrintWriter(s.getOutputStream())
        output.write(params[0].toString())
        output.flush()
        val inStream = BufferedInputStream(s.getInputStream())
        val bytes = ByteArray(100)
        var returnValue = ""
        val count = inStream.read(bytes, 0, 100)
        if (count >= 0) {
            returnValue =  bytes.decodeToString()
        }
        output.close()
        s.close()
        return returnValue
    }
}

