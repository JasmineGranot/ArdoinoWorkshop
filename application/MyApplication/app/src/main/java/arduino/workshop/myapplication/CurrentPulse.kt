package arduino.workshop.myapplication

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_current_pulse.*
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch


class CurrentPulse : AppCompatActivity() {
    @ExperimentalStdlibApi
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_current_pulse)
        CoroutineScope(Dispatchers.IO).launch {
            val currentPulseFromServer = ClientSocket.doInBackground("getHeartbeat;102")
            currentPulse.text = currentPulseFromServer
        }
    }

}