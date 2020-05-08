package arduino.workshop.myapplication

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.main_screen.*
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.launch


class ScreenMain: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main_screen)

        getCurrentPulseButton.setOnClickListener {
            /*CoroutineScope(IO).launch {
                val currentPulse = ClientSocket.doInBackground("getHeartbeat")
            }*/
            startActivity(Intent(this, CurrentPulse::class.java))
        }

        emergencyCallButton.setOnClickListener {
            startActivity(Intent(this, EmergencyCall::class.java))
        }

        getFallHistoryButton.setOnClickListener {
            startActivity(Intent(this, FallHistory::class.java))
        }

        getPulseHistoryButton.setOnClickListener {
            startActivity(Intent(this, PulseHistory::class.java))
        }
    }
}