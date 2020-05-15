package arduino.workshop.myapplication

import android.os.AsyncTask
import kotlinx.coroutines.Dispatchers
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.InetSocketAddress
import java.net.Socket

object ClientSocket : AsyncTask<String, Void, String>() {
    public override fun doInBackground(vararg params: String?): String? {
        val s = Socket("10.0.2.2", 65432)
        val output = PrintWriter(s.getOutputStream())
        output.write(params[0].toString())
        output.flush()
        val input =
            BufferedReader(InputStreamReader(s.getInputStream()))
        output.println(input)
        output.close()
        s.close()
        return input.toString()
    }
}

