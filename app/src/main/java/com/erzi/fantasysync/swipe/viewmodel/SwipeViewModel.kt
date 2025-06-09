package com.erzi.fantasysync.swipe.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.erzi.fantasysync.swipe.data.SwipeRepository
import com.erzi.fantasysync.swipe.model.FantasyCard
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

/**
 * ViewModel for the swipe deck screen.
 */
class SwipeViewModel(private val repository: SwipeRepository) : ViewModel() {

    /**
     * Exposes the current cards as a [StateFlow] for UI consumption.
     */
    val cards: StateFlow<List<FantasyCard>> = repository.cards
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

    /**
     * Handles a swipe event on [card].
     */
    fun swipe(card: FantasyCard) {
        viewModelScope.launch {
            repository.swipe(card)
        }
    }
}
