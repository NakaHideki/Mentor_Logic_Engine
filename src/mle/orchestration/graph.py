"""
状態管理マシン (LangGraph)

ユーザーの学習履歴や問題の文脈を管理
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum


class SessionState(Enum):
    """セッションの状態"""
    IDLE = "idle"  # 待機中
    ANALYZING = "analyzing"  # 解析中
    WAITING_USER_INPUT = "waiting_user_input"  # ユーザー入力待ち
    PROVIDING_HINT = "providing_hint"  # ヒント提供中
    COMPLETED = "completed"  # 完了


@dataclass
class ProblemContext:
    """問題の文脈情報"""
    problem_statement: str  # 問題文
    test_type: str  # 検定の種類（例: "one_sample_t_test"）
    variables: Dict[str, Any]  # 変数定義（例: {"μ": "population_mean", "n": 30}）
    step_history: List[str]  # これまでのステップ（LaTeX）
    last_error_type: Optional[str] = None  # 最後に検出されたエラー


class StateMachine:
    """
    LangGraphを使用した状態管理エンジン
    
    Attributes:
        current_state: 現在の状態
        context: 問題の文脈情報
    """
    
    def __init__(self):
        self.current_state = SessionState.IDLE
        self.context: Optional[ProblemContext] = None
    
    def start_session(
        self,
        problem_statement: str,
        test_type: str,
        variables: Dict[str, Any]
    ) -> None:
        """
        新しい学習セッションを開始
        
        Args:
            problem_statement: 問題文
            test_type: 検定の種類
            variables: 変数定義
        """
        # TODO: セッションを初期化
        raise NotImplementedError("セッション開始処理を実装してください")
    
    def add_step(self, step: str) -> None:
        """
        ユーザーの新しいステップを記録
        
        Args:
            step: LaTeX形式のステップ
        """
        # TODO: step_historyに追加
        raise NotImplementedError("ステップ追加処理を実装してください")
    
    def transition_to(self, new_state: SessionState) -> None:
        """
        状態遷移
        
        Args:
            new_state: 遷移先の状態
        """
        # TODO: 状態遷移のロジックとバリデーション
        raise NotImplementedError("状態遷移処理を実装してください")
    
    def get_context(self) -> Optional[ProblemContext]:
        """
        現在の文脈情報を取得
        
        Returns:
            問題の文脈情報
        """
        return self.context
    
    def build_graph(self) -> Any:
        """
        LangGraphのグラフを構築
        
        Returns:
            LangGraphのグラフオブジェクト
        """
        # TODO: LangGraphを使ってワークフローグラフを構築
        # ノード: Perception -> Reasoning -> Verification -> Response
        raise NotImplementedError("グラフ構築処理を実装してください")
