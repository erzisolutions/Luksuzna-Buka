package com.erzi.fantasysync.swipe.ui

import androidx.compose.foundation.gestures.detectDragGestures
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.material.Card
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.consume
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.erzi.fantasysync.swipe.model.FantasyCard
import com.erzi.fantasysync.swipe.viewmodel.SwipeViewModel
import kotlin.math.abs
import kotlin.math.roundToInt

@Composable
fun SwipeDeckScreen(viewModel: SwipeViewModel) {
    val cards by viewModel.cards.collectAsState()

    Box(modifier = Modifier.fillMaxSize()) {
        cards.asReversed().forEach { card ->
            SwipeableCard(card = card, onSwiped = { viewModel.swipe(card) })
        }
    }
}

@Composable
private fun SwipeableCard(card: FantasyCard, onSwiped: () -> Unit) {
    var offsetX by remember { mutableStateOf(0f) }
    val threshold = 150f

    Box(
        modifier = Modifier
            .offset { IntOffset(offsetX.roundToInt(), 0) }
            .pointerInput(card.id) {
                detectDragGestures(
                    onDragEnd = {
                        if (abs(offsetX) > threshold) onSwiped()
                        offsetX = 0f
                    }
                ) { change, dragAmount ->
                    change.consume()
                    offsetX += dragAmount.x
                }
            }
    ) {
        Card(elevation = 8.dp) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text(text = card.title, style = MaterialTheme.typography.h6, fontSize = 20.sp)
                Text(text = card.description)
            }
        }
    }
}
