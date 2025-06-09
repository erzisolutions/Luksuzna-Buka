package com.erzi.fantasysync.swipe.data

import com.erzi.fantasysync.swipe.model.FantasyCard
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.update

/**
 * Provides access to swipe deck data.
 */
interface SwipeRepository {
    /** Flow of cards currently in the deck. */
    val cards: Flow<List<FantasyCard>>

    /**
     * Removes the given card from the deck.
     */
    suspend fun swipe(card: FantasyCard)
}

/**
 * Simple in-memory implementation of [SwipeRepository].
 */
class InMemorySwipeRepository(initialCards: List<FantasyCard>) : SwipeRepository {
    private val _cards = MutableStateFlow(initialCards)
    override val cards: Flow<List<FantasyCard>> = _cards

    override suspend fun swipe(card: FantasyCard) {
        _cards.update { list -> list.filter { it.id != card.id } }
    }
}
