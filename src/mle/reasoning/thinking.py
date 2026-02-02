"""
考え中エンジン (Thinking Logic)

Chain-of-Thoughtを用いてユーザーの論理ミスを特定
"""

from typing import Dict, Any, List, Optional
from enum import Enum


class ErrorType(Enum):
    """論理エラーの種類"""
    WRONG_TEST = "wrong_statistical_test"  # 検定手法の誤り
    VARIABLE_CONFUSION = "variable_confusion"  # 変数の混同
    FORMULA_ERROR = "formula_error"  # 公式の誤り
    CALCULATION_ERROR = "calculation_error"  # 計算ミス
    ASSUMPTION_VIOLATION = "assumption_violation"  # 前提条件の違反


class ThinkingEngine:
    """
    ユーザーの思考プロセスをデバッグするエンジン
    
    Attributes:
        model_name: 使用する推論モデル
    """
    
    def __init__(self, model_name: str = "qwen3-thinking"):
        """
        Args:
            model_name: 推論に使用するモデル名
        """
        self.model_name = model_name
    
    def identify_logic_error(
        self,
        current_step: str,
        previous_steps: List[str],
        problem_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        現在のステップから論理エラーを特定
        
        Args:
            current_step: ユーザーの現在の式（LaTeX）
            previous_steps: これまでのステップのリスト
            problem_context: 問題文や変数定義などの文脈情報
            
        Returns:
            エラー分析結果:
                - has_error: bool - エラーがあるか
                - error_type: Optional[ErrorType] - エラーの種類
                - error_location: str - エラーの箇所
                - reasoning: str - エラーと判断した理由（思考過程）
                - suggested_question: str - ユーザーへの問いかけ
        
        Example:
            >>> engine = ThinkingEngine()
            >>> result = engine.identify_logic_error(
            ...     current_step=r"z = \frac{x - \mu}{\sigma}",
            ...     previous_steps=[...],
            ...     problem_context={"test_type": "one_sample_mean", "n": 30}
            ... )
            >>> print(result['suggested_question'])
            "標本平均の検定では、標準誤差はどう表されますか？"
        """
        # TODO: LLMを使って論理ミスを特定
        # ヒント: Chain-of-Thoughtで段階的に分析
        raise NotImplementedError("論理エラー特定処理を実装してください")
    
    def generate_socratic_question(
        self,
        error_type: ErrorType,
        context: Dict[str, Any]
    ) -> str:
        """
        ソクラテス式の問いかけを生成
        
        「答えを教えず、気づきを促す」問いかけ
        
        Args:
            error_type: 特定されたエラーの種類
            context: 問題の文脈情報
            
        Returns:
            問いかけ文字列
        """
        # TODO: エラータイプに応じた問いかけを生成
        raise NotImplementedError("問いかけ生成処理を実装してください")
    
    def find_shortest_path_to_correct(
        self,
        current_step: str,
        correct_solution: str
    ) -> List[str]:
        """
        現在の式から正解への最短経路を逆算
        
        Args:
            current_step: 現在のユーザーの式
            correct_solution: 正しい解法
            
        Returns:
            ヒントのリスト（段階的な導き）
        """
        # TODO: 正解までの最短経路を計算
        raise NotImplementedError("経路計算処理を実装してください")
