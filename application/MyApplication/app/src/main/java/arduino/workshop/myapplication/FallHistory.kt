package arduino.workshop.myapplication

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch


class FallHistory: AppCompatActivity() {
    @ExperimentalStdlibApi
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fall_history)
        CoroutineScope(Dispatchers.IO).launch {
            val currentPulseFromServer = ClientSocket.doInBackground("getFallHistory 100")
        }
    }
}