package arduino.workshop.myapplication

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.main_screen.*

class ScreenMain: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main_screen)

        getLocationButton.setOnClickListener {
            startActivity(Intent(this, Location::class.java))
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