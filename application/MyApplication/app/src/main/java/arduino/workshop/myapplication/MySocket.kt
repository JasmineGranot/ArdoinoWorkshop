package arduino.workshop.myapplication

import android.os.AsyncTask
import java.net.Socket

object MySocket : AsyncTask<String, Void, String>() {
    var s = Socket()

    @ExperimentalStdlibApi
    public override fun doInBackground(vararg params: String?): String? {
        //val s = Socket("10.0.2.2", 65432)
        s = Socket("192.168.1.13", 65432)
        return "true"
    }

    public fun getSocket() : Socket {
        return s
    }

    fun closeSocket(){
        s.close()
    }
}